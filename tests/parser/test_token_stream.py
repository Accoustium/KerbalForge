import pytest

from kerbalforge.models import TokenType
from kerbalforge.parser import Tokenizer, TokenStream


def test_peek_does_not_consume() -> None:
    stream = TokenStream(Tokenizer("{"))

    token = stream.peek()

    assert token.type is TokenType.LBRACE

    token = stream.peek()

    assert token.type is TokenType.LBRACE


def test_peek_returns_same_object() -> None:
    stream = TokenStream(Tokenizer("{"))

    first = stream.peek()
    second = stream.peek()

    assert first is second


def test_consume() -> None:
    stream = TokenStream(Tokenizer("{}"))

    assert stream.consume().type is TokenType.LBRACE

    assert stream.consume().type is TokenType.RBRACE


def test_peek_after_next() -> None:
    stream = TokenStream(Tokenizer("{}"))

    stream.consume()

    assert stream.peek().type is TokenType.RBRACE


def test_expect_success() -> None:
    stream = TokenStream(Tokenizer("{"))

    token = stream.expect(TokenType.LBRACE)

    assert token.type is TokenType.LBRACE


def test_expect_failure() -> None:
    stream = TokenStream(Tokenizer("{"))

    with pytest.raises(SyntaxError):
        stream.expect(TokenType.RBRACE)


def test_tokenstream_peek_offset() -> None:
    stream = TokenStream(
        Tokenizer(
            """
MODULE
{
}
"""
        )
    )

    assert stream.peek_type() is TokenType.IDENTIFIER
    assert stream.peek_type(1) is TokenType.LBRACE


def test_peek_two_tokens() -> None:
    stream = TokenStream(Tokenizer("MODULE\n{\n}\n"))

    assert stream.peek().type is TokenType.IDENTIFIER
    assert stream.peek(1).type is TokenType.LBRACE

    # Ensure peeking didn't consume anything
    assert stream.consume().type is TokenType.IDENTIFIER
    assert stream.consume().type is TokenType.LBRACE
