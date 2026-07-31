from kerbalforge.parser import Tokenizer, TokenType


def test_left_brace():
    tokenizer = Tokenizer("{")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.LBRACE


def test_right_brace():
    tokenizer = Tokenizer("}")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.RBRACE


def test_equals():
    tokenizer = Tokenizer("=")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.EQUALS


def test_identifier():
    tokenizer = Tokenizer("PART")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.IDENTIFIER
    assert tokens[0].value == "PART"


def test_multiple_identifiers():
    tokens = list(Tokenizer("PART MODULE"))

    assert tokens[0].value == "PART"
    assert tokens[1].value == "MODULE"


def test_eof_token():
    tokens = list(Tokenizer("PART"))

    assert tokens[-1].type is TokenType.EOF


def test_empty_input():
    tokens = list(Tokenizer(""))

    assert len(tokens) == 1
    assert tokens[0].type is TokenType.EOF


def test_ignore_spaces():
    tokens = list(Tokenizer("     PART     "))

    assert tokens[0].value == "PART"


def test_ignore_tabs():
    tokens = list(Tokenizer("\t\tPART\t"))

    assert tokens[0].value == "PART"


def test_ignore_blank_lines():
    tokens = list(Tokenizer("\n\n\nPART\n\n"))

    assert tokens[0].value == "PART"


def test_assignment():
    tokens = list(Tokenizer("part = probeCoreOcto2_v2"))

    assert [t.value for t in tokens[:-1]] == [
        "part",
        "=",
        "probeCoreOcto2_v2",
    ]


def test_position_vector():
    tokens = list(Tokenizer("pos = 0.0,1.25,-3.0"))

    assert tokens[2].value == "0.0,1.25,-3.0"


def test_resource_block():
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
        TokenType.IDENTIFIER,
        TokenType.RBRACE,
    ]
