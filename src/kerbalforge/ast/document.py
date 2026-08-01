from dataclasses import dataclass, field

from .statement import Node


@dataclass(slots=True)
class Document:
    nodes: list[Node] = field(default_factory=list)
