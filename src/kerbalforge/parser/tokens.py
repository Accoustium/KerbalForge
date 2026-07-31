from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    IDENTIFIER = auto()
    EQUALS = auto()
    LBRACE = auto()
    RBRACE = auto()
    EOF = auto()


@dataclass(slots=True, frozen=True)
class Token:
    type: TokenType
    value: str
    line: int
    column: int
