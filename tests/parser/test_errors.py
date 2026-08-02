from kerbalforge.diagnostics import ParseError, SourceLocation, SourceSpan, UnexpectedEOFError, UnexpectedTokenError
from kerbalforge.models import Token, TokenType


def test_parse_error_message() -> None:
    error = ParseError("Something went wrong")

    assert str(error) == "Something went wrong"


def test_parse_error_span() -> None:
    span = SourceSpan(
        SourceLocation(1, 1),
        SourceLocation(1, 5),
    )

    error = ParseError(
        "Oops",
        span,
    )

    assert error.span == span


def test_unexpected_token_error() -> None:
    token = Token(
        TokenType.LBRACE,
        "{",
        line=4,
        column=7,
    )

    error = UnexpectedTokenError(
        TokenType.EQUALS,
        token,
    )

    assert error.expected is TokenType.EQUALS
    assert error.actual is token


def test_unexpected_eof_error() -> None:
    span = SourceSpan(
        SourceLocation(8, 1),
        SourceLocation(8, 1),
    )

    error = UnexpectedEOFError(span)

    assert error.span == span
