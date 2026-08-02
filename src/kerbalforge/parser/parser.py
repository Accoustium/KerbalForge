from collections.abc import Iterable

from kerbalforge.ast import Document, Node, Property, Statement
from kerbalforge.models import Token, TokenType

from .token_stream import TokenStream


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
        if self._stream.peek_type(1) is TokenType.LBRACE:
            return self._parse_node()

        return self._parse_property()

    def _parse_property(self) -> Property:
        key = self._stream.expect_identifier()

        self._stream.expect(TokenType.EQUALS)

        value = self._stream.expect_identifier()

        return Property(
            key=key,
            value=value,
        )
