#!/usr/bin/env python3
"""Render data/cosmic-count.json into a human-readable COSMIC CFP markdown report.

Usage:
    python3 render_markdown.py <cosmic-count.json> [output.md]

If output.md is omitted, prints to stdout. Layout mirrors the reference report:
disclaimer -> roll-up + per-epic summary table -> per-epic sections
(functional processes with movement tables, measurement gaps, caveats) ->
COSMIC v5.0 movement-pattern primer.
"""
import json
import os
import sys


def esc(text) -> str:
    """Escape pipes and collapse newlines so a cell stays on one table row."""
    return str(text or "").replace("|", "\\|").replace("\n", " ").strip()


def fp_cfp(fp) -> int:
    """Per-process CFP: explicit `cfp` field, else count of dataMovements."""
    cfp = fp.get("cfp")
    if cfp is not None:
        return cfp
    return len(fp.get("dataMovements", []) or [])


def render(data) -> str:
    out = []
    w = out.append

    w("# COSMIC Functional-Size Measurement (CFP)\n")

    disclaimer = data.get("disclaimer")
    if disclaimer:
        w(f"> **Disclaimer.** {disclaimer}\n")

    roll = data.get("rollUp", {})
    epics = data.get("epics", [])

    # ---- Roll-up -----------------------------------------------------------
    w("## Roll-up\n")
    total = roll.get("projectCfpCountable", 0)
    cfp_range = roll.get("cfpRange") or [0, total]
    # tolerate malformed cfpRange (wrong length) — pad/truncate to [low, high]
    if len(cfp_range) < 2:
        cfp_range = [cfp_range[0] if cfp_range else 0, total]
    measured = roll.get("epicsMeasured", len(epics))
    epics_total = roll.get("epicsTotal", measured)
    countable = roll.get("countableEpics", "")
    resting = roll.get("epicsRestingOnAssumptions", []) or []
    failed = roll.get("epicsFailed", []) or []

    w("| Metric | Value |")
    w("|---|---|")
    w(f"| Project CFP (countable) | **{total}** |")
    w(f"| CFP range (Confirmed floor → measured) | **{cfp_range[0]} – {cfp_range[1]}** |")
    w(f"| Epics measured | {measured} of {epics_total} |")
    w(f"| Countable epics | {countable} |")
    w(f"| Epics resting on assumptions | {len(resting)} of {epics_total} |")
    if failed:
        w(f"| Epics failed to measure (excluded) | {len(failed)}: {esc(', '.join(failed))} |")
    w("")

    if failed:
        w(f"> **⚠ Partial count.** {len(failed)} epic(s) failed to measure and are "
          f"EXCLUDED from the roll-up: {esc(', '.join(failed))}. Re-run to size them.\n")

    if resting:
        w(f"*Range note: the low bound ({cfp_range[0]}) is the sum of "
          f"**Confirmed** epics only. {len(resting)} of {epics_total} epics rest "
          f"on assumptions and should be re-measured against built artifacts.*\n")

    # ---- Per-epic summary --------------------------------------------------
    w("### Per-epic summary\n")
    w("| Epic | Name | CFP | Confidence | Processes | Gaps |")
    w("|---|---|---|---|---|---|")
    gap_total = 0
    for e in epics:
        procs = e.get("functionalProcesses", []) or []
        n_gaps = len(e.get("gaps", []) or [])
        gap_total += n_gaps
        w(f"| {esc(e.get('epicId'))} | {esc(e.get('epicName'))} | "
          f"**{e.get('epicCfp', 0)}** | {esc(e.get('confidence'))} | "
          f"{len(procs)} | {n_gaps} |")
    w(f"| | **Total** | **{total}** | | | {gap_total} |")
    w("\n---\n")

    # ---- Data groups catalog ----------------------------------------------
    # Flatten every functional process's dataGroups[] into one table keyed by
    # epic + FP. Omitted cleanly when no process carries the field.
    dg_rows = []
    for e in epics:
        eid = e.get("epicId", "")
        for fp in e.get("functionalProcesses", []) or []:
            label = fp.get("functionalProcessId") or (fp.get("artifact", {}) or {}).get("name")
            for dg in fp.get("dataGroups", []) or []:
                dg_rows.append((eid, label, dg.get("name"), dg.get("description")))
    if dg_rows:
        w("## Data groups\n")
        w("| Epic | FP | Data group | Description |")
        w("|---|---|---|---|")
        for eid, label, name, desc in dg_rows:
            w(f"| {esc(eid)} | {esc(label)} | {esc(name)} | {esc(desc)} |")
        w("\n---\n")

    # ---- Per-epic detail ---------------------------------------------------
    for e in epics:
        eid = e.get("epicId", "")
        w(f"## {esc(e.get('epicId'))} — {esc(e.get('epicName'))}\n")
        w(f"**Epic CFP: {e.get('epicCfp', 0)} · Confidence: {esc(e.get('confidence'))}**\n")

        users = e.get("functionalUsers", []) or []
        if users:
            w("**Functional users:** " + " · ".join(esc(u) for u in users) + "\n")

        for i, fp in enumerate(e.get("functionalProcesses", []) or [], start=1):
            label = fp.get("functionalProcessId") or (fp.get("artifact", {}) or {}).get("name")
            w(f"### FP{i} — {esc(label)} — {fp_cfp(fp)} CFP")
            w("")
            moves = fp.get("dataMovements", []) or []
            if moves:
                w("| # | Move | Data group | Note | Citation |")
                w("|---|---|---|---|---|")
                for n, m in enumerate(moves, start=1):
                    w(f"| {n} | **{esc(m.get('movementType'))}** | {esc(m.get('dataGroupRef'))} | "
                      f"{esc(m.get('note'))} | {esc(m.get('citation'))} |")
                w("")

        gaps = e.get("gaps", []) or []
        if gaps:
            w(f"### Measurement gaps ({eid})\n")
            for g in gaps:
                w(f"**{esc(g.get('gapId'))} · {esc(g.get('category'))}** — "
                  f"{g.get('gapOrQuestion', '').strip()}\n")
                impact = g.get("impactOrNotes", "").strip()
                if impact:
                    w(f"*Impact:* {impact}\n")

        caveats = e.get("caveats", []) or []
        if caveats:
            w(f"### Caveats & modeling choices ({eid})\n")
            for c in caveats:
                w(f"- {str(c).strip()}")
            w("")

        w("---\n")

    # ---- Primer ------------------------------------------------------------
    primer = data.get("rulesPrimer")
    if primer:
        w("## COSMIC v5.0 Movement-Pattern Primer (Salesforce delivery scope)\n")
        w(primer.strip())
        w("")

    return "\n".join(out)


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit("usage: render_markdown.py <cosmic-count.json> [output.md]")

    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)

    md = render(data)

    if len(sys.argv) == 3:
        out_dir = os.path.dirname(sys.argv[2])
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(md)
        print(f"wrote {sys.argv[2]}")
    else:
        sys.stdout.write(md)


if __name__ == "__main__":
    main()
