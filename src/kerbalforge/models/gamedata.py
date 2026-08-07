from dataclasses import dataclass
from pathlib import Path

from kerbalforge.ast import Document


@dataclass(slots=True, frozen=True)
class GameDataFile:
    path: Path
    document: Document
