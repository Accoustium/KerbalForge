from kerbalforge.models import TokenType
from kerbalforge.parser import Tokenizer


def test_left_brace() -> None:
    tokenizer = Tokenizer("{")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.LBRACE


def test_right_brace() -> None:
    tokenizer = Tokenizer("}")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.RBRACE


def test_equals() -> None:
    tokenizer = Tokenizer("=")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.EQUALS


def test_identifier() -> None:
    tokenizer = Tokenizer("PART")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.IDENTIFIER
    assert tokens[0].value == "PART"


def test_multiple_identifiers() -> None:
    tokens = list(Tokenizer("PART MODULE"))

    assert tokens[0].value == "PART"
    assert tokens[1].value == "MODULE"


def test_eof_token() -> None:
    tokens = list(Tokenizer("PART"))

    assert tokens[-1].type is TokenType.EOF


def test_empty_input() -> None:
    tokens = list(Tokenizer(""))

    assert len(tokens) == 1
    assert tokens[0].type is TokenType.EOF


def test_ignore_spaces() -> None:
    tokens = list(Tokenizer("     PART     "))

    assert tokens[0].value == "PART"


def test_ignore_tabs() -> None:
    tokens = list(Tokenizer("\t\tPART\t"))

    assert tokens[0].value == "PART"


def test_ignore_blank_lines() -> None:
    tokens = list(Tokenizer("\n\n\nPART\n\n"))

    assert tokens[0].value == "PART"


def test_assignment() -> None:
    tokens = list(Tokenizer("part = probeCoreOcto2_v2"))

    assert [t.value for t in tokens[:-1]] == [
        "part",
        "=",
        "probeCoreOcto2_v2",
    ]


def test_position_vector() -> None:
    tokens = list(Tokenizer("pos = 0.0,1.25,-3.0"))

    assert tokens[2].value == "0.0,1.25,-3.0"


def test_resource_block() -> None:
    tokens = list(
        Tokenizer(
            """
RESOURCE
{
    name = LiquidFuel
}
"""
        )
    )

    assert [t.type for t in tokens[:-1]] == [
        TokenType.IDENTIFIER,
        TokenType.LBRACE,
        TokenType.IDENTIFIER,
        TokenType.EQUALS,
        TokenType.PROPERTY_VALUE,
        TokenType.RBRACE,
    ]


def test_spaced_name() -> None:
    tokens = list(
        Tokenizer(
            """
ship = My Craft
"""
        )
    )

    assert tokens[0].value == "ship"
    assert tokens[2].value == "My Craft"


def test_empty_property() -> None:
    tokens = list(
        Tokenizer(
            """
description =
"""
        )
    )

    assert tokens[0].value == "description"
    assert tokens[2].value == ""


def test_version_as_str() -> None:
    tokens = list(
        Tokenizer(
            """
version = 1.12.5
"""
        )
    )

    assert tokens[0].value == "version"
    assert tokens[2].value == "1.12.5"


def test_multi_break_property() -> None:
    tokens = list(
        Tokenizer(
            """
attN = bottom,Null_0_0|-1|0
"""
        )
    )

    assert tokens[0].value == "attN"
    assert tokens[2].value == "bottom,Null_0_0|-1|0"
