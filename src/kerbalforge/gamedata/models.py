from dataclasses import dataclass

from kerbalforge.ast import Document


@dataclass(slots=True)
class PartDefinition:
    name: str
    title: str

    document: Document
