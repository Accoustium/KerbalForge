import pytest

from kerbalforge.ast import Node, Property, child_nodes, find_property, first_child, required_property
from kerbalforge.diagnostics import ResolutionError


def test_find_property_returns_matching_property() -> None:
    node = Node(
        name="PART",
        body=[
            Property(key="name", value="probeCore"),
            Property(key="title", value="Probodobodyne OKTO"),
        ],
    )

    result = find_property(node, "title")

    assert result is not None
    assert result.value == "Probodobodyne OKTO"


def test_find_property_returns_none_when_missing() -> None:
    node = Node(
        name="PART",
        body=[
            Property(key="name", value="probeCore"),
        ],
    )

    result = find_property(node, "title")

    assert result is None


def test_required_property_returns_matching_property() -> None:
    node = Node(
        name="PART",
        body=[
            Property(key="name", value="probeCore"),
        ],
    )

    result = required_property(node, "name")

    assert result.value == "probeCore"


def test_required_property_raises_resolution_error() -> None:
    node = Node(
        name="PART",
        body=[
            Property(key="name", value="probeCore"),
        ],
    )

    with pytest.raises(ResolutionError, match="title"):
        required_property(node, "title")


def test_child_nodes_returns_matching_nodes() -> None:
    module_one = Node(name="MODULE")
    module_two = Node(name="MODULE")

    node = Node(
        name="PART",
        body=[
            Property(key="name", value="probeCore"),
            module_one,
            Node(name="RESOURCE"),
            module_two,
        ],
    )

    result = child_nodes(node, "MODULE")

    assert result == [module_one, module_two]


def test_child_nodes_ignores_properties() -> None:
    node = Node(
        name="PART",
        body=[
            Property(key="MODULE", value="not-a-node"),
            Node(name="MODULE"),
        ],
    )

    result = child_nodes(node, "MODULE")

    assert len(result) == 1
    assert isinstance(result[0], Node)


def test_child_nodes_returns_empty_list_when_missing() -> None:
    node = Node(
        name="PART",
        body=[
            Node(name="RESOURCE"),
        ],
    )

    assert child_nodes(node, "MODULE") == []


def test_child_nodes_does_not_search_nested_nodes() -> None:
    nested = Node(name="MODULE")

    node = Node(
        name="PART",
        body=[
            Node(
                name="WRAPPER",
                body=[nested],
            ),
        ],
    )

    assert child_nodes(node, "MODULE") == []


def test_first_child_returns_first_matching_node() -> None:
    first = Node(name="MODULE")
    second = Node(name="MODULE")

    node = Node(
        name="PART",
        body=[
            first,
            second,
        ],
    )

    assert first_child(node, "MODULE") is first


def test_first_child_ignores_later_matching_nodes() -> None:
    first = Node(name="MODULE")
    second = Node(name="MODULE")

    node = Node(
        name="PART",
        body=[first, second],
    )

    result = first_child(node, "MODULE")

    assert result is first
    assert result is not second


def test_first_child_returns_none_when_missing() -> None:
    node = Node(
        name="PART",
        body=[
            Node(name="RESOURCE"),
        ],
    )

    assert first_child(node, "MODULE") is None


def test_first_child_does_not_search_nested_nodes() -> None:
    nested = Node(name="MODULE")

    node = Node(
        name="PART",
        body=[
            Node(
                name="WRAPPER",
                body=[nested],
            ),
        ],
    )

    assert first_child(node, "MODULE") is None
