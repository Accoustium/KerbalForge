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

    assert SourceLocation(line=token.line, column=token.column) == SourceLocation(
        line=4,
        column=17,
    )


def test_single_location_span() -> None:
    location = SourceLocation(3, 8)

    assert SourceSpanner.single(location) == SourceSpan(
        start=location,
        end=location,
    )


def test_between_locations() -> None:
    start = SourceLocation(1, 1)
    end = SourceLocation(5, 3)

    assert SourceSpanner.between(start, end) == SourceSpan(
        start=start,
        end=end,
    )
