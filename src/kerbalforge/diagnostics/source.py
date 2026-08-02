from dataclasses import dataclass

from kerbalforge.models import Token


@dataclass(frozen=True, slots=True)
class SourceLocation:
    line: int
    column: int

    def __str__(self) -> str:
        return f"{self.line}:{self.column}"


@dataclass(frozen=True, slots=True)
class SourceSpan:
    start: Token | SourceLocation
    end: Token | SourceLocation

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"
