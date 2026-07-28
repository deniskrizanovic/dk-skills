"""Pytest setup: put scripts/ on sys.path."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_CFP_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS = _CFP_ROOT / "scripts"

if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))


@pytest.fixture(scope="session")
def cfp_root() -> Path:
    return _CFP_ROOT
