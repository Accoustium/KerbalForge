from pathlib import Path


class GameDataScanner:
    """Finds all KSP configuration files."""

    def scan(self, root: Path) -> list[Path]:
        return sorted(root.rglob("*.cfg"))
