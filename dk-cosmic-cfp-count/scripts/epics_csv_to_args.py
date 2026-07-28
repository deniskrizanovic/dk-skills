#!/usr/bin/env python3
"""Convert an epics CSV into the JSON `args` the cosmic-cfp-count workflow consumes.

Usage:
    python3 epics_csv_to_args.py <epics.csv>

Prints a JSON object {"epics": [...]} to stdout. Redirect to a file and hand the
path to the workflow, or read it and pass inline as Workflow args.

Column mapping (case-insensitive, flexible on separators/spacing):
    Epic ID       -> epic_id      (required)
    Epic Name     -> epic_name    (required)
    Description   -> description  (required — the FUR text the measurement rests on)
    Confidence    -> confidence   (optional; default "Assumed")
    Depends On    -> depends_on   (optional; split on ';' or ',')

Any additional columns are passed through under their normalized (snake_case)
key, so an enriched CSV still reaches the measure agent as context.
"""
import csv
import json
import re
import sys


def norm(key: str) -> str:
    """Normalize a header to snake_case for tolerant matching."""
    return re.sub(r"[^a-z0-9]+", "_", (key or "").strip().lower()).strip("_")


# canonical field -> ordered accepted normalized headers (first match wins;
# ordered list, NOT a set, so precedence is deterministic across runs)
FIELD_ALIASES = {
    "epic_id": ["epic_id", "id", "item_id"],
    "epic_name": ["epic_name", "name", "epic", "title"],
    "description": ["description", "desc", "fur", "requirement", "requirements"],
    "confidence": ["confidence"],
    "depends_on": ["depends_on", "dependencies", "depends"],
}


def resolve(headers):
    """Map each canonical field to the actual header present, if any."""
    # keep the FIRST header for each normalized form — two headers that collide
    # (e.g. "Epic ID" and "Epic-ID" both -> "epic_id") must not let the later,
    # likely-junk column win resolution over the canonical one
    norm_to_actual = {}
    for h in headers:
        norm_to_actual.setdefault(norm(h), h)
    resolved = {}
    for field, aliases in FIELD_ALIASES.items():
        for alias in aliases:
            if alias in norm_to_actual:
                resolved[field] = norm_to_actual[alias]
                break
    return resolved, norm_to_actual


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: epics_csv_to_args.py <epics.csv>")

    path = sys.argv[1]
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            sys.exit(f"error: {path} has no header row")

        resolved, norm_to_actual = resolve(reader.fieldnames)

        missing = [f for f in ("epic_id", "epic_name", "description") if f not in resolved]
        if missing:
            sys.exit(
                f"error: could not find required column(s) {missing} in headers "
                f"{reader.fieldnames}. Expected an 'Epic ID', 'Epic Name', and "
                f"'Description' column (aliases accepted)."
            )

        # headers already claimed by a canonical field — don't double-emit them
        claimed = set(resolved.values())

        epics = []
        for row_num, row in enumerate(reader, start=2):
            epic_id = (row.get(resolved["epic_id"]) or "").strip()
            if not epic_id:
                continue  # skip blank/spacer rows

            epic = {
                "epic_id": epic_id,
                "epic_name": (row.get(resolved["epic_name"]) or "").strip(),
                "description": (row.get(resolved["description"]) or "").strip(),
            }

            if "confidence" in resolved:
                conf = (row.get(resolved["confidence"]) or "").strip()
                epic["confidence"] = conf or "Assumed"

            if "depends_on" in resolved:
                raw = (row.get(resolved["depends_on"]) or "").strip()
                deps = [d.strip() for d in re.split(r"[;,]", raw) if d.strip()]
                epic["depends_on"] = deps

            # pass through any extra columns as snake_case context, but never
            # let a normalized extra header (e.g. "Epic-ID" -> "epic_id")
            # clobber a value already set from a resolved canonical column
            for header, value in row.items():
                if header in claimed or header is None:
                    continue
                key = norm(header)
                if key in epic:
                    continue
                val = (value or "").strip()
                if val:
                    epic[key] = val

            epics.append(epic)

    if not epics:
        sys.exit(f"error: no epic rows found in {path}")

    json.dump({"epics": epics}, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
