from __future__ import annotations

from enum import Enum, auto


class TokenType(Enum):
    IDENTIFIER = auto()
    EQUALS = auto()
    LBRACE = auto()
    RBRACE = auto()
    EOF = auto()
