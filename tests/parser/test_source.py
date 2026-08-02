from kerbalforge.diagnostics import (
    SourceLocation,
    SourceSpan,
    SourceSpanner,
)
from kerbalforge.models import Token, TokenType


def test_token_location() -> None:
    token = Token(
        TokenType.IDENTIFIER,
        "PART",
        line=4,
        column=17,
    )

    assert SourceSpanner.location(line=token.line, column=token.column) == SourceLocation(
        line=4,
        column=17,
    )


def test_single_location_span() -> None:
    token = Token(
        TokenType.IDENTIFIER,
        "PART",
        line=4,
        column=17,
    )

    assert SourceSpanner.token(token) == SourceSpan(
        start=SourceSpanner.location(line=token.line, column=token.column),
        end=SourceSpanner.location(line=token.line, column=token.column),
    )


def test_between_locations() -> None:
    start = Token(
        TokenType.IDENTIFIER,
        "PART",
        line=4,
        column=17,
    )
    end = Token(
        TokenType.IDENTIFIER,
        "PART",
        line=5,
        column=23,
    )

    assert SourceSpanner.between(start, end) == SourceSpan(
        start=SourceSpanner.location(start.line, start.column), end=SourceSpanner.location(end.line, end.column)
    )
