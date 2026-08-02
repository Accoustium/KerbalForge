from __future__ import annotations

from dataclasses import dataclass

# from kerbalforge.diagnostics import SourceLocation, SourceSpan, SourceSpanner
from .token_type import TokenType


@dataclass(slots=True, frozen=True)
class Token:
    type: TokenType
    value: str
    line: int
    column: int

    # @property
    # def location(self) -> SourceLocation:
    #     return SourceLocation(
    #         self.line,
    #         self.column,
    #     )

    # @property
    # def span(self) -> SourceSpan:
    #     return SourceSpanner.single(
    #         self.location,
    #     )
