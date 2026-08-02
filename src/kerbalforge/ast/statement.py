from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field

from kerbalforge.diagnostics import SourceSpan


class Statement(ABC):  # noqa: B024
    """Base class for all AST statements."""

    span: SourceSpan | None = None


@dataclass(slots=True)
class Property(Statement):
    key: str
    value: str


@dataclass(slots=True)
class Node(Statement):
    name: str
    body: list[Statement] = field(default_factory=list)

    def add(self, statement: Statement) -> None:
        self.body.append(statement)
