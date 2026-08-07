from kerbalforge.diagnostics import (
    ParseError,
    ResolutionError,
    SourceLocation,
    SourceSpan,
    UnexpectedEOFError,
    UnexpectedTokenError,
)
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


def test_resolution_error_is_diagnostic_error() -> None:
    error = ResolutionError("Unable to resolve part.")

    assert isinstance(error, ResolutionError)


def test_resolution_error_message() -> None:
    error = ResolutionError("Unable to resolve part.")

    assert str(error) == "Unable to resolve part."


def test_resolution_error_with_span() -> None:
    span = SourceSpan(
        SourceLocation(1, 1),
        SourceLocation(1, 10),
    )

    error = ResolutionError(
        "Unable to resolve part.",
        span,
    )

    assert error.span == span
    assert "Unable to resolve part." in str(error)
