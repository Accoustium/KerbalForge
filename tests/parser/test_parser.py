from kerbalforge.ast import Property
from kerbalforge.parser import Parser, Tokenizer


def test_parse_empty_part() -> None:
    parser = Parser(Tokenizer("PART\n{\n}\n"))

    document = parser.parse()

    assert len(document.nodes) == 1

    assert document.nodes[0].name == "PART"


def test_parse_single_property() -> None:
    parser = Parser(
        Tokenizer(
            """
PART
{
    part = probeCoreOcto2_v2
}
"""
        )
    )

    document = parser.parse()

    node = document.nodes[0]

    assert len(node.body) == 1

    prop = node.body[0]

    assert isinstance(prop, Property)
    assert prop.key == "part"
    assert prop.value == "probeCoreOcto2_v2"
