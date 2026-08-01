from collections.abc import Iterable

from kerbalforge.ast import Document, Node, Property, Statement

from .token_stream import TokenStream
from .tokens import Token, TokenType


class Parser:
    def __init__(self, tokens: Iterable[Token]) -> None:
        self._stream = TokenStream(tokens)

    def parse(self) -> Document:
        document = Document()

        while not self._stream.eof:
            document.nodes.append(self._parse_node())

        return document

    def _parse_node(self) -> Node:
        name = self._stream.expect_identifier()

        self._stream.expect(TokenType.LBRACE)

        node = Node(name=name)

        while self._stream.peek().type is not TokenType.RBRACE:
            node.add(self._parse_statement())

        self._stream.expect(TokenType.RBRACE)

        return node

    def _parse_statement(self) -> Statement:
        return self._parse_property()

    def _parse_property(self) -> Property:
        key = self._stream.expect_identifier()

        self._stream.expect(TokenType.EQUALS)

        value = self._stream.expect_identifier()

        return Property(
            key=key,
            value=value,
        )
