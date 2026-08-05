from collections.abc import Iterable

from kerbalforge.ast import Document, Node, Property, Statement
from kerbalforge.diagnostics import SourceSpanner
from kerbalforge.models import Token, TokenType

from .token_stream import TokenStream


class Parser:
    def __init__(self, tokens: Iterable[Token]) -> None:
        self._stream = TokenStream(tokens)

    def parse(self) -> Document:
        document = Document()

        while not self._stream.eof:
            document.body.append(self._parse_statement())

        return document

    def _parse_node(self) -> Node:
        start = self._stream.expect_identifier()

        node = Node(
            name=start.value,
        )

        self._stream.expect(TokenType.LBRACE)

        while self._stream.peek_type() is not TokenType.RBRACE:
            node.add(self._parse_statement())

        end = self._stream.expect(TokenType.RBRACE)

        node.span = SourceSpanner.between(
            start,
            end,
        )

        return node

    def _parse_statement(self) -> Statement:
        if self._stream.peek_type(1) is TokenType.LBRACE:
            return self._parse_node()

        return self._parse_property()

    def _parse_property(self) -> Property:
        key = self._stream.expect(TokenType.IDENTIFIER)
        self._stream.expect(TokenType.EQUALS)
        value = self._stream.expect(TokenType.PROPERTY_VALUE)

        return Property(
            key=key.value,
            value=value.value,
            span=SourceSpanner.between(
                key,
                value,
            ),
        )
