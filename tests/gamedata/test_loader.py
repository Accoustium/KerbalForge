from pathlib import Path

from kerbalforge.ast import Node, Property
from kerbalforge.gamedata import GameDataLoader, GameDataScanner


def test_scanner_finds_cfg_files(tmp_path: Path) -> None:
    (tmp_path / "Part.cfg").write_text("")
    (tmp_path / "Readme.txt").write_text("")

    scanner = GameDataScanner()

    files = scanner.scan(tmp_path)

    assert len(files) == 1
    assert files[0].name == "Part.cfg"


def test_scanner_recursive(tmp_path: Path) -> None:
    folder = tmp_path / "Squad" / "Parts"

    folder.mkdir(parents=True)

    (folder / "probe.cfg").write_text("")
    (folder / "tank.cfg").write_text("")

    scanner = GameDataScanner()

    assert len(scanner.scan(tmp_path)) == 2


def test_loader_returns_document(engine_cfg: Path) -> None:
    loader = GameDataLoader()

    document = loader.load_file(engine_cfg)

    assert len(document.body) > 0

    part = next(s for s in document.body if isinstance(s, Node))

    assert part.name == "PART"

    name = next(s for s in part.body if isinstance(s, Property) and s.key == "name")

    assert name.value == "liquidEngineMini_v2"
