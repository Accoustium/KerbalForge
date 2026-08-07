from pathlib import Path

from kerbalforge.ast import Document
from kerbalforge.parser import Parser, Tokenizer

from .scanner import GameDataScanner


class GameDataLoader:
    """Loads KSP configuration files."""

    def load_file(self, path: Path) -> Document:
        text = path.read_text(encoding="utf-8-sig")

        return Parser(
            Tokenizer(text),
        ).parse()

    def load_directory(
        self,
        root: Path,
    ) -> list[Document]:
        scanner = GameDataScanner()

        return [self.load_file(path) for path in scanner.scan(root)]
