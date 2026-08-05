from __future__ import annotations

from enum import Enum, auto


class TokenType(Enum):
    IDENTIFIER = auto()
    PROPERTY_VALUE = auto()
    LBRACE = auto()
    RBRACE = auto()
    EQUALS = auto()
    EOF = auto()
