import pytest

from kerbalforge.ast import Node, Property
from kerbalforge.diagnostics import UnexpectedEOFError, UnexpectedTokenError
from kerbalforge.parser import Parser, Tokenizer


def test_parse_empty_part() -> None:
    parser = Parser(Tokenizer("PART\n{\n}\n"))

    document = parser.parse()

    body = document.body
    node = body[0]

    assert len(body) == 1

    assert isinstance(node, Node)
    assert node.name == "PART"


def test_parse_single_property() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
    part = probeCoreOcto2_v2
}
"""
        )
    )

    document = parser.parse()

    node = document.body[0]

    assert isinstance(node, Node)
    assert len(node.body) == 1

    prop = node.body[0]

    assert isinstance(prop, Property)
    assert prop.key == "part"
    assert prop.value == "probeCoreOcto2_v2"


def test_parse_multiple_property() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
    part = probeCore

    pos = 0,0,0
}
"""
        )
    )

    document = parser.parse()

    node = document.body[0]

    assert isinstance(node, Node)
    assert len(node.body) == 2

    prop = node.body[0]

    assert isinstance(prop, Property)
    assert prop.key == "part"
    assert prop.value == "probeCore"

    prop = node.body[1]

    assert isinstance(prop, Property)
    assert prop.key == "pos"
    assert prop.value == "0,0,0"


def test_parse_nested_node() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
    MODULE
    {
    }
}
"""
        )
    )

    document = parser.parse()

    part = document.body[0]

    assert isinstance(part, Node)
    assert len(part.body) == 1

    module = part.body[0]

    assert isinstance(module, Node)
    assert module.name == "MODULE"
    assert module.body == []


def test_parse_mixed_node() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
    part = probeCore

    MODULE
    {
    }

    pos = 0,0,0
}
"""
        )
    )

    document = parser.parse()

    part = document.body[0]

    assert isinstance(part, Node)

    assert isinstance(part.body[0], Property)
    assert isinstance(part.body[1], Node)
    assert isinstance(part.body[2], Property)


def test_missing_left_brace() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
}
"""
        )
    )

    with pytest.raises(UnexpectedTokenError):
        parser.parse()


def test_missing_right_brace() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
"""
        )
    )

    with pytest.raises(UnexpectedEOFError):
        parser.parse()


def test_property_missing_equals() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
    part probeCore
}
"""
        )
    )

    with pytest.raises(UnexpectedTokenError):
        parser.parse()


def test_property_has_span() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
    part = probeCore
}
"""
        )
    )

    document = parser.parse()

    node = document.body[0]

    assert isinstance(node, Node)

    prop = node.body[0]

    assert prop.span.start.line == 4
    assert prop.span.end.line == 4


def test_node_has_span() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
}
"""
        )
    )

    document = parser.parse()

    assert document.body[0].span is not None


def test_nested_node_has_span() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
    MODULE
    {
    }
}
"""
        )
    )

    document = parser.parse()

    node = document.body[0]

    assert isinstance(node, Node)
    module = node.body[0]

    assert isinstance(module, Node)
    assert module.span is not None
