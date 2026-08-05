from dataclasses import dataclass, field

from .statement import Statement


@dataclass(slots=True)
class Document:
    body: list[Statement] = field(default_factory=list)
