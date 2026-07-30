"""Unit tests for render_markdown (cosmic-count.json -> markdown)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from render_markdown import esc, fp_cfp, main, render


# ---- helpers --------------------------------------------------------------

def minimal_report(**over):
    """A schema-shaped report; override any top-level or rollUp key."""
    roll = {
        "projectCfpCountable": 10,
        "cfpRange": [7, 10],
        "epicsMeasured": 1,
        "epicsTotal": 1,
        "countableEpics": 1,
        "epicsRestingOnAssumptions": [],
    }
    roll.update(over.pop("rollUp", {}))
    report = {
        "disclaimer": "test disclaimer",
        "rollUp": roll,
        "epics": [
            {
                "epicId": "E01",
                "epicName": "Login",
                "epicCfp": 10,
                "confidence": "Assumed",
                "functionalUsers": ["End User"],
                "functionalProcesses": [
                    {
                        "functionalProcessId": "FP1-Login",
                        "artifact": {"type": "epic", "name": "Login"},
                        "cfp": 3,
                        "dataMovements": [
                            {"name": "creds", "order": 1, "movementType": "E",
                             "dataGroupRef": "Credentials", "note": "entry",
                             "citation": "m#L1"},
                        ],
                    }
                ],
                "gaps": [],
            }
        ],
        "measurementGaps": [],
    }
    report.update(over)
    return report


# ---- esc ------------------------------------------------------------------

def test_esc_escapes_pipes_and_collapses_newlines():
    assert esc("a|b") == "a\\|b"
    assert esc("line1\nline2") == "line1 line2"


def test_esc_handles_none_and_numbers():
    assert esc(None) == ""
    assert esc(5) == "5"


# ---- fp_cfp ---------------------------------------------------------------

def test_fp_cfp_prefers_explicit_field():
    assert fp_cfp({"cfp": 4, "dataMovements": [1, 2]}) == 4


def test_fp_cfp_falls_back_to_movement_count():
    assert fp_cfp({"dataMovements": [1, 2, 3]}) == 3


def test_fp_cfp_zero_when_no_movements():
    assert fp_cfp({}) == 0


def test_fp_cfp_explicit_zero_beats_fallback():
    # cfp is 0 (not None) -> honored, not overridden by len(dataMovements).
    assert fp_cfp({"cfp": 0, "dataMovements": [1, 2]}) == 0


# ---- render: structure ----------------------------------------------------

def test_render_includes_core_sections():
    md = render(minimal_report())
    assert "# COSMIC Functional-Size Measurement (CFP)" in md
    assert "> **Disclaimer.** test disclaimer" in md
    assert "## Roll-up" in md
    assert "### Per-epic summary" in md
    assert "## E01 — Login" in md
    assert "FP1 — FP1-Login — 3 CFP" in md


def test_render_movement_table_row():
    md = render(minimal_report())
    assert "| # | Move | Data group | Note | Citation |" in md
    assert "| 1 | **E** | Credentials | entry | m#L1 |" in md


def test_render_functional_users_line():
    md = render(minimal_report())
    assert "**Functional users:** End User" in md


def test_render_primer_section_when_present():
    md = render(minimal_report(rulesPrimer="Rule 1: E for entry."))
    assert "## COSMIC v5.0 Movement-Pattern Primer" in md
    assert "Rule 1: E for entry." in md


def test_render_omits_primer_when_absent():
    md = render(minimal_report())
    assert "Movement-Pattern Primer" not in md


def test_render_gaps_section():
    md = render(minimal_report(epics=[{
        "epicId": "E02", "epicName": "Vague", "epicCfp": 0,
        "confidence": "Unknown", "functionalProcesses": [],
        "gaps": [{"gapId": "CG-E02-01", "category": "Measurement Gap",
                  "gapOrQuestion": "How many roles?", "impactOrNotes": "±3 CFP"}],
    }]))
    assert "### Measurement gaps (E02)" in md
    assert "CG-E02-01" in md
    assert "How many roles?" in md
    assert "*Impact:* ±3 CFP" in md


def test_render_caveats_section():
    ep = minimal_report()["epics"][0] | {"caveats": ["assumed one role"]}
    md = render(minimal_report(epics=[ep]))
    assert "### Caveats & modeling choices (E01)" in md
    assert "- assumed one role" in md


# ---- render: data groups catalog -----------------------------------------

def test_render_data_groups_section_present():
    ep = minimal_report()["epics"][0]
    ep["functionalProcesses"][0]["dataGroups"] = [
        {"name": "Lost Pet Report", "description": "Caller details, pet species."},
        {"name": "Microchip Record", "description": "Registry match."},
    ]
    md = render(minimal_report(epics=[ep]))
    assert "## Data groups" in md
    assert "| Epic | FP | Data group | Description |" in md
    assert "| E01 | FP1-Login | Lost Pet Report | Caller details, pet species. |" in md
    assert "| E01 | FP1-Login | Microchip Record | Registry match. |" in md


def test_render_omits_data_groups_when_absent():
    md = render(minimal_report())
    assert "## Data groups" not in md


# ---- render: cfpRange robustness (bug #6) --------------------------------

def test_render_tolerates_short_cfp_range():
    md = render(minimal_report(rollUp={"cfpRange": [7]}))
    # pads [7] -> [7, total(10)] instead of raising IndexError
    assert "**7 – 10**" in md


def test_render_tolerates_empty_cfp_range():
    md = render(minimal_report(rollUp={"cfpRange": []}))
    assert "**0 – 10**" in md


def test_render_defaults_missing_cfp_range():
    r = minimal_report()
    del r["rollUp"]["cfpRange"]
    md = render(r)
    assert "**0 – 10**" in md


# ---- render: failed epics (bug #5) ---------------------------------------

def test_render_surfaces_failed_epics():
    md = render(minimal_report(rollUp={"epicsFailed": ["E09", "E10"],
                                       "epicsTotal": 3}))
    assert "Epics failed to measure (excluded)" in md
    assert "E09, E10" in md
    assert "**⚠ Partial count.**" in md


def test_render_no_partial_banner_when_none_failed():
    md = render(minimal_report())
    assert "Partial count" not in md


def test_render_range_note_when_epics_rest_on_assumptions():
    md = render(minimal_report(rollUp={"epicsRestingOnAssumptions": ["E01"],
                                       "epicsTotal": 2, "cfpRange": [7, 10]}))
    assert "*Range note: the low bound (7) is the sum of" in md
    assert "1 of 2 epics rest" in md


def test_render_no_range_note_when_all_confirmed():
    md = render(minimal_report())  # empty epicsRestingOnAssumptions
    assert "Range note" not in md


# ---- main: file output (bug #1) ------------------------------------------

def test_main_creates_nested_output_dir(tmp_path, capsys, monkeypatch):
    src = tmp_path / "cc.json"
    src.write_text(json.dumps(minimal_report()), encoding="utf-8")
    out = tmp_path / "outputs" / "artifacts" / "report.md"
    monkeypatch.setattr("sys.argv", ["render_markdown.py", str(src), str(out)])
    main()
    assert out.exists()
    assert "# COSMIC Functional-Size Measurement (CFP)" in out.read_text(encoding="utf-8")


def test_main_writes_to_cwd_without_dir(tmp_path, capsys, monkeypatch):
    # bare filename (no dirname) must not crash on makedirs("")
    src = tmp_path / "cc.json"
    src.write_text(json.dumps(minimal_report()), encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.argv", ["render_markdown.py", str(src), "report.md"])
    main()
    assert (tmp_path / "report.md").exists()


def test_main_prints_to_stdout_without_output_arg(tmp_path, capsys, monkeypatch):
    src = tmp_path / "cc.json"
    src.write_text(json.dumps(minimal_report()), encoding="utf-8")
    monkeypatch.setattr("sys.argv", ["render_markdown.py", str(src)])
    main()
    assert "# COSMIC Functional-Size Measurement (CFP)" in capsys.readouterr().out


def test_main_wrong_arg_count_exits(monkeypatch):
    monkeypatch.setattr("sys.argv", ["render_markdown.py"])
    with pytest.raises(SystemExit) as exc:
        main()
    assert "usage" in str(exc.value)
