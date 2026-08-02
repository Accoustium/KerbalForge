from __future__ import annotations

from kerbalforge.models import Token, TokenType

from .source import SourceSpan
from .spanner import SourceSpanner


class DiagnosticError(Exception):
    """Base class for all KerbalForge diagnostics."""

    def __init__(
        self,
        message: str,
        span: SourceSpan | None = None,
    ) -> None:
        super().__init__(message)

        self.message = message
        self.span = span

    def __str__(self) -> str:
        if self.span is None:
            return self.message

        return f"{self.message} ({self.span})"


class ParseError(DiagnosticError):
    """Raised when parsing fails."""


class UnexpectedEOFError(ParseError):
    """Unexpected end of input."""

    def __init__(
        self,
        span: SourceSpan | None = None,
    ) -> None:
        super().__init__(
            "Unexpected end of input.",
            span,
        )


class UnexpectedTokenError(ParseError):
    def __init__(
        self,
        expected: TokenType,
        actual: Token,
    ) -> None:
        self.expected = expected
        self.actual = actual

        super().__init__(
            f"Expected {expected.name}, got {actual.type.name}.",
            SourceSpanner.token(actual),
        )
