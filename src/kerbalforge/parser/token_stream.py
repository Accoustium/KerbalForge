from __future__ import annotations

from collections.abc import Iterable, Iterator

from .tokens import Token, TokenType


class TokenStream:
    """Provides look-ahead and controlled consumption of a token stream."""

    def __init__(self, tokens: Iterable[Token]) -> None:
        self._iterator: Iterator[Token] = iter(tokens)
        self._buffer: Token | None = None

    def peek(self, offset: int = 0) -> Token:
        """Return the next token without consuming it."""

        if self._buffer is None:
            self._buffer = next(self._iterator)

        return self._buffer

    @property
    def eof(self) -> bool:
        return self.peek().type is TokenType.EOF

    def consume(self) -> Token:
        """Consume and return the next token."""

        token = self.peek()

        self._buffer = None

        return token

    def match(self, token_type: TokenType) -> bool:
        """Consume the next token if it matches."""

        if self.peek().type is token_type:
            self.consume()
            return True

        return False

    def consume_if(self, token_type: TokenType) -> Token | None:
        """Consume and return the next token if it matches."""

        if self.peek().type is token_type:
            return self.consume()

        return None

    def expect(self, token_type: TokenType) -> Token:
        token = self.peek()

        if token.type is not token_type:
            raise SyntaxError(f"Expected {token_type.name}, got {token.type.name}")

        return self.consume()

    def expect_identifier(self) -> str:
        token = self.expect(TokenType.IDENTIFIER)

        return token.value
