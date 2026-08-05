from collections.abc import Callable

import pytest

from kerbalforge.ast import Document, Node, Property


def test_cs001_parses(parse_fixture: Callable[[str], Document]) -> None:
    document = parse_fixture("cs-001-minimal.craft")

    assert len(document.body) > 0

    ship = document.body[0]
    assert isinstance(ship, Property)
    assert ship.key == "ship"
    assert ship.value == "cs-001-minimal"

    part = next(s for s in document.body if isinstance(s, Node) and s.name == "PART")

    assert len(part.body) > 0


@pytest.mark.parametrize(  # type: ignore[misc]
    "fixture",
    [
        "cs-001-minimal.craft",
        "cs-002-stack.craft",
        "cs-003-engine.craft",
        "cs-004-symmetry.craft",
        "cs-005-science.craft",
        "cs-006-power.craft",
        "cs-007-docking.craft",
        "cs-008-action-groups.craft",
        "cs-009-advanced.craft",
        "cs-010-large.craft",
    ],
)
def test_fixture_parses(fixture: str, parse_fixture: Callable[[str], Document]) -> None:
    document = parse_fixture(fixture)

    assert len(document.body) > 0
