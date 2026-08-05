from kerbalforge.ast import Document, Node, Property


def test_node_name() -> None:
    node = Node("PART")

    assert node.name == "PART"


def test_node_has_no_children() -> None:
    node = Node("PART")

    assert node.body == []


def test_property() -> None:
    prop = Property("part", "probeCore")

    assert prop.key == "part"
    assert prop.value == "probeCore"


def test_document_empty() -> None:
    document = Document()

    assert document.body == []
