from pathlib import Path

import pytest

from kerbalforge.ast import Document
from kerbalforge.parser import Parser, Tokenizer

TESTS_ROOT = Path(__file__).resolve().parent
FIXTURES_ROOT = TESTS_ROOT / "fixtures"
CRAFT_FIXTURES = FIXTURES_ROOT / "craft"


def load_fixture(name: str) -> str:
    if not CRAFT_FIXTURES.exists():
        raise FileNotFoundError(f"Fixture directory not found: {CRAFT_FIXTURES}")

    return (CRAFT_FIXTURES / name).read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def parse_fixture():
    def _parse_fixture(name: str) -> Document:
        return Parser(Tokenizer(load_fixture(name))).parse()

    return _parse_fixture
