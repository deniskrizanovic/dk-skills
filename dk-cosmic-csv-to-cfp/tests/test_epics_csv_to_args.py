"""Unit tests for epics_csv_to_args (CSV -> workflow args)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

import epics_csv_to_args as mod
from epics_csv_to_args import FIELD_ALIASES, main, norm, resolve


# ---- helpers --------------------------------------------------------------

def run(tmp_path: Path, csv_text: str, capsys, monkeypatch):
    """Write csv_text to a temp file, run main(), return parsed stdout JSON.

    Encodes as UTF-8 with BOM to also exercise the utf-8-sig read path.
    """
    path = tmp_path / "epics.csv"
    path.write_text(csv_text, encoding="utf-8-sig")
    monkeypatch.setattr("sys.argv", ["epics_csv_to_args.py", str(path)])
    main()
    return json.loads(capsys.readouterr().out)


# ---- norm -----------------------------------------------------------------

def test_norm_lowercases_and_snakecases():
    assert norm("Epic ID") == "epic_id"
    assert norm("Depends On") == "depends_on"
    assert norm("  Epic-Name  ") == "epic_name"


def test_norm_collapses_runs_and_strips_edges():
    assert norm("Epic   //  ID") == "epic_id"
    assert norm("__Epic__") == "epic"
    assert norm(None) == ""
    assert norm("") == ""


# ---- resolve --------------------------------------------------------------

def test_resolve_maps_canonical_aliases():
    resolved, _ = resolve(["Epic ID", "Title", "Requirement"])
    assert resolved["epic_id"] == "Epic ID"
    assert resolved["epic_name"] == "Title"       # alias of epic_name
    assert resolved["description"] == "Requirement"  # alias of description


def test_resolve_first_wins_on_normalized_collision():
    # "Epic ID" and "Epic-ID" both normalize to "epic_id"; the first header
    # must win so a later junk column can't hijack the canonical mapping.
    resolved, norm_to_actual = resolve(["Epic ID", "Epic-ID", "Name", "Desc"])
    assert resolved["epic_id"] == "Epic ID"
    assert norm_to_actual["epic_id"] == "Epic ID"


def test_resolve_alias_precedence_is_deterministic():
    # Both "id" and "item_id" are epic_id aliases. Ordered list -> "epic_id"
    # canonical alias tried first, so an explicit "Epic ID" always wins over
    # a bare "ID"/"Item ID" regardless of column order.
    resolved, _ = resolve(["ID", "Item ID", "Epic ID", "Name", "Desc"])
    assert resolved["epic_id"] == "Epic ID"


def test_resolve_missing_optional_fields_absent():
    resolved, _ = resolve(["Epic ID", "Name", "Desc"])
    assert "confidence" not in resolved
    assert "depends_on" not in resolved


# ---- main: happy path -----------------------------------------------------

def test_main_parses_rows(tmp_path, capsys, monkeypatch):
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description\n"
        "E01,Login,SSO federated login\n"
        "E02,Search,Full text search\n",
        capsys,
        monkeypatch,
    )
    assert [e["epic_id"] for e in out["epics"]] == ["E01", "E02"]
    assert out["epics"][0]["epic_name"] == "Login"
    assert out["epics"][1]["description"] == "Full text search"


def test_main_confidence_defaults_to_assumed(tmp_path, capsys, monkeypatch):
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description,Confidence\n"
        "E01,Login,SSO,Confirmed\n"
        "E02,Search,FTS,\n",  # blank confidence -> default
        capsys,
        monkeypatch,
    )
    assert out["epics"][0]["confidence"] == "Confirmed"
    assert out["epics"][1]["confidence"] == "Assumed"


def test_main_no_confidence_column_omits_field(tmp_path, capsys, monkeypatch):
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description\nE01,Login,SSO\n",
        capsys,
        monkeypatch,
    )
    assert "confidence" not in out["epics"][0]


def test_main_splits_depends_on(tmp_path, capsys, monkeypatch):
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description,Depends On\n"
        'E03,Checkout,Cart to order,"E01; E02 , E04"\n',  # quoted: comma stays in cell
        capsys,
        monkeypatch,
    )
    assert out["epics"][0]["depends_on"] == ["E01", "E02", "E04"]


def test_main_empty_depends_on_is_empty_list(tmp_path, capsys, monkeypatch):
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description,Depends On\nE01,Login,SSO,\n",
        capsys,
        monkeypatch,
    )
    assert out["epics"][0]["depends_on"] == []


# ---- main: row handling ---------------------------------------------------

def test_main_skips_blank_id_rows(tmp_path, capsys, monkeypatch):
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description\n"
        "E01,Login,SSO\n"
        ",,\n"           # spacer row
        "  ,Filler,x\n"  # whitespace-only id
        "E02,Search,FTS\n",
        capsys,
        monkeypatch,
    )
    assert [e["epic_id"] for e in out["epics"]] == ["E01", "E02"]


def test_main_passes_through_extra_columns_as_snake_case(tmp_path, capsys, monkeypatch):
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description,Business Value\n"
        "E01,Login,SSO,High\n",
        capsys,
        monkeypatch,
    )
    assert out["epics"][0]["business_value"] == "High"


def test_main_extra_column_never_clobbers_canonical(tmp_path, capsys, monkeypatch):
    # "Epic-ID" is an unclaimed extra column that normalizes to "epic_id".
    # It must NOT overwrite the value resolved from the real "Epic ID" column.
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description,Epic-ID\n"
        "E01,Login,SSO,JUNK\n",
        capsys,
        monkeypatch,
    )
    assert out["epics"][0]["epic_id"] == "E01"


def test_main_ignores_none_header_overflow_cells(tmp_path, capsys, monkeypatch):
    # A row with more fields than headers: csv.DictReader keys the overflow
    # under None. The pass-through loop must skip header is None (norm(None)
    # would otherwise emit a bogus "" key).
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description\n"
        "E01,Login,SSO,EXTRA1,EXTRA2\n",
        capsys,
        monkeypatch,
    )
    assert out["epics"][0]["epic_id"] == "E01"
    assert "" not in out["epics"][0]
    assert None not in out["epics"][0]


def test_main_blank_extra_column_omitted(tmp_path, capsys, monkeypatch):
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description,Notes\n"
        "E01,Login,SSO,\n",
        capsys,
        monkeypatch,
    )
    assert "notes" not in out["epics"][0]


def test_main_reads_utf8_bom_and_unicode(tmp_path, capsys, monkeypatch):
    # run() writes with utf-8-sig, so the BOM path is always exercised; assert
    # a non-ASCII value round-trips (ensure_ascii=False in the dump).
    out = run(
        tmp_path,
        "Epic ID,Epic Name,Description\nE01,Café Menu,Прейскурант\n",
        capsys,
        monkeypatch,
    )
    assert out["epics"][0]["epic_name"] == "Café Menu"
    assert out["epics"][0]["description"] == "Прейскурант"


# ---- main: error paths ----------------------------------------------------

def test_main_missing_required_column_exits(tmp_path, capsys, monkeypatch):
    with pytest.raises(SystemExit) as exc:
        run(tmp_path, "Epic ID,Description\nE01,SSO\n", capsys, monkeypatch)
    assert "epic_name" in str(exc.value)


def test_main_no_header_exits(tmp_path, capsys, monkeypatch):
    path = tmp_path / "empty.csv"
    path.write_text("", encoding="utf-8")
    monkeypatch.setattr("sys.argv", ["epics_csv_to_args.py", str(path)])
    with pytest.raises(SystemExit) as exc:
        main()
    assert "no header row" in str(exc.value)


def test_main_no_data_rows_exits(tmp_path, capsys, monkeypatch):
    with pytest.raises(SystemExit) as exc:
        run(tmp_path, "Epic ID,Epic Name,Description\n", capsys, monkeypatch)
    assert "no epic rows" in str(exc.value)


def test_main_wrong_arg_count_exits(monkeypatch):
    monkeypatch.setattr("sys.argv", ["epics_csv_to_args.py"])
    with pytest.raises(SystemExit) as exc:
        main()
    assert "usage" in str(exc.value)


# ---- config sanity --------------------------------------------------------

def test_field_aliases_are_ordered_lists():
    # Ordered lists (not sets) keep alias precedence deterministic across runs.
    for aliases in FIELD_ALIASES.values():
        assert isinstance(aliases, list)
    assert FIELD_ALIASES["epic_id"][0] == "epic_id"
