#!/usr/bin/env bash
# tokencost-setup/install.sh
# Usage: bash /path/to/tokencost-setup/install.sh
# Run from the root of the target project.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOKS_DIR="$HOME/.claude/hooks"
PROJECT_DIR="$(pwd)"
TOKENCOST_DIR="$PROJECT_DIR/tokencost"
SETTINGS_FILE="$PROJECT_DIR/.claude/settings.json"

# ── Step 1: Global install (idempotent) ──────────────────────────────────────

if [ -f "$HOOKS_DIR/cost-tracker.py" ]; then
    echo "Global scripts already installed at $HOOKS_DIR — skipping."
else
    echo "Installing global scripts to $HOOKS_DIR ..."
    mkdir -p "$HOOKS_DIR"
    cp "$SCRIPT_DIR/scripts/cost-tracker.py"           "$HOOKS_DIR/cost-tracker.py"
    cp "$SCRIPT_DIR/scripts/generate_token_tracker.py" "$HOOKS_DIR/generate_token_tracker.py"
    cp "$SCRIPT_DIR/scripts/sum-cost.py"               "$HOOKS_DIR/sum-cost.py"
    chmod +x "$HOOKS_DIR/cost-tracker.py"
    chmod +x "$HOOKS_DIR/generate_token_tracker.py"
    chmod +x "$HOOKS_DIR/sum-cost.py"
    echo "  Installed: cost-tracker.py, generate_token_tracker.py, sum-cost.py"
fi

# ── Step 2: Per-project scaffold ─────────────────────────────────────────────

mkdir -p "$TOKENCOST_DIR"

CSV_FILE="$TOKENCOST_DIR/cost.csv"
if [ -f "$CSV_FILE" ]; then
    echo "cost.csv already exists — skipping."
else
    echo "session_id,started_at,ended_at,end_reason,total_cost_usd,input_tokens,output_tokens,cache_creation_tokens,cache_read_tokens,total_tokens,models,git_branch" > "$CSV_FILE"
    echo "  Created: tokencost/cost.csv"
fi

CONFIG_FILE="$TOKENCOST_DIR/config.json"
if [ -f "$CONFIG_FILE" ]; then
    echo "config.json already exists — skipping."
else
    echo ""
    echo "Configure tokencost for this project:"

    # branch_pattern
    read -rp "  Branch pattern regex (default: issue/(\\d+)): " branch_pattern
    branch_pattern="${branch_pattern:-issue/(\\d+)}"

    # output_path
    read -rp "  Report output path relative to repo root (default: docs/economics/token-tracker.md): " output_path
    output_path="${output_path:-docs/economics/token-tracker.md}"

    # repo_url — auto-detect, let user confirm/override
    detected_url=""
    if git remote get-url origin &>/dev/null; then
        raw_url="$(git remote get-url origin)"
        # Normalise SSH -> HTTPS
        if [[ "$raw_url" =~ ^git@ ]]; then
            detected_url="$(echo "$raw_url" | sed 's|git@\([^:]*\):\(.*\)\.git$|https://\1/\2|; s|git@\([^:]*\):\(.*\)$|https://\1/\2|')"
        else
            detected_url="${raw_url%.git}"
        fi
    fi

    if [ -n "$detected_url" ]; then
        read -rp "  Repo URL (detected: $detected_url — press Enter to accept): " repo_url
        repo_url="${repo_url:-$detected_url}"
    else
        read -rp "  Repo URL (e.g. https://github.com/owner/repo): " repo_url
    fi

    python3 - <<PYEOF
import json, pathlib
config = {
    "branch_pattern": "$branch_pattern",
    "output_path": "$output_path",
    "repo_url": "$repo_url",
}
pathlib.Path("$CONFIG_FILE").write_text(json.dumps(config, indent=2) + "\n")
PYEOF
    echo "  Created: tokencost/config.json"
fi

# ── Step 3: Wire hooks in .claude/settings.json ───────────────────────────────

mkdir -p "$PROJECT_DIR/.claude"

export SETTINGS_FILE HOOKS_DIR
python3 - <<'PYEOF'
import json, os, sys
from pathlib import Path

settings_file = Path(os.environ["SETTINGS_FILE"])
hooks_dir = os.environ["HOOKS_DIR"]

if settings_file.exists():
    try:
        settings = json.loads(settings_file.read_text())
    except json.JSONDecodeError:
        print(f"warning: could not parse {settings_file} — creating fresh", file=sys.stderr)
        settings = {}
else:
    settings = {}

hooks = settings.setdefault("hooks", {})

FINALIZE_CMD = f"python3 {hooks_dir}/cost-tracker.py finalize"
BACKFILL_CMD = f"python3 {hooks_dir}/cost-tracker.py backfill"

def ensure_hook(event: str, cmd: str):
    entries = hooks.setdefault(event, [])
    # Support both flat list of strings and list of hook objects
    existing_cmds = set()
    for entry in entries:
        if isinstance(entry, str):
            existing_cmds.add(entry)
        elif isinstance(entry, dict):
            for h in entry.get("hooks", []):
                existing_cmds.add(h.get("command", ""))
    if cmd in existing_cmds:
        print(f"  Hook already present for {event} — skipping.")
        return
    entries.append({"matcher": "", "hooks": [{"type": "command", "command": cmd}]})
    print(f"  Wired {event} hook.")

ensure_hook("SessionEnd", FINALIZE_CMD)
ensure_hook("SessionStart", BACKFILL_CMD)

settings_file.write_text(json.dumps(settings, indent=2) + "\n")
PYEOF

# ── Step 4: Summary ───────────────────────────────────────────────────────────

echo ""
echo "tokencost setup complete."
echo ""
echo "Next steps:"
echo "  - Add 'tokencost/cost.csv' to .gitignore if you don't want to commit session data."
echo "  - Run 'python3 ~/.claude/hooks/generate_token_tracker.py' from this repo to generate the report."
echo "  - Run 'python3 ~/.claude/hooks/sum-cost.py' for a quick cost summary (reads tokencost/cost.csv from CWD)."
PYEOF
