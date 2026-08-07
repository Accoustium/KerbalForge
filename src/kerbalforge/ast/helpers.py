from __future__ import annotations

from kerbalforge.diagnostics import ResolutionError

from .statement import Node, Property


def find_property(
    node: Node,
    key: str,
) -> Property | None:
    for statement in node.body:
        if isinstance(statement, Property) and statement.key == key:
            return statement

    return None


def required_property(
    node: Node,
    key: str,
) -> Property:
    property = find_property(node, key)

    if property is None:
        raise ResolutionError(f"Required property '{key}' was not found.")

    return property


def child_nodes(
    node: Node,
    name: str,
) -> list[Node]:
    return [statement for statement in node.body if isinstance(statement, Node) and statement.name == name]


def first_child(
    node: Node,
    name: str,
) -> Node | None:
    nodes = child_nodes(node, name)

    if not nodes:
        return None

    return nodes[0]
