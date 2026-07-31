import pytest

from kerbalforge.parser import Tokenizer, TokenStream, TokenType


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
