from __future__ import annotations

from collections import deque
from collections.abc import Iterable, Iterator

from kerbalforge.models import Token, TokenType


class TokenStream:
    """Provides look-ahead and controlled consumption of a token stream."""

    def __init__(self, tokens: Iterable[Token]) -> None:
        self._iterator: Iterator[Token] = iter(tokens)
        self._buffer: deque[Token] = deque()

    def _fill(self, count: int) -> None:
        while len(self._buffer) <= count:
            try:
                self._buffer.append(next(self._iterator))
            except StopIteration as exc:
                raise SyntaxError("Unexpected end of input") from exc

    def peek(self, offset: int = 0) -> Token:
        self._fill(offset)
        return self._buffer[offset]

    def consume(self) -> Token:
        self._fill(0)
        return self._buffer.popleft()

    def peek_type(self, offset: int = 0) -> TokenType:
        return self.peek(offset).type

    @property
    def eof(self) -> bool:
        return self.peek().type is TokenType.EOF

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

    def expect_identifier(self) -> Token:
        token = self.expect(TokenType.IDENTIFIER)

        return token
