from __future__ import annotations

from typing import Self

from kerbalforge.models import Token, TokenType


class Tokenizer:
    def __init__(self, text: str) -> None:
        self.text = text
        self.index = 0
        self.line = 1
        self.column = 1
        self._finished = False
        self._expect_property_value = False

    def __iter__(self) -> Self:
        return self

    def tokenize(self) -> list[Token]:
        """Temporary compatibility wrapper."""
        return list(self)

    def __next__(self) -> Token:
        if self._finished:
            raise StopIteration

        while not self._eof():
            ch = self._peek()

            if self._expect_property_value:
                self._expect_property_value = False
                return self._read_property_value()

            if ch in " \t\r":
                self._advance()
                continue

            if ch == "\n":
                self._advance_line()
                continue

            if ch == "{":
                token = self._make(TokenType.LBRACE, "{")
                self._advance()
                return token

            if ch == "}":
                token = self._make(TokenType.RBRACE, "}")
                self._advance()
                return token

            if ch == "=":
                token = self._make(TokenType.EQUALS, "=")
                self._advance()
                self._expect_property_value = True
                return token

            return self._read_identifier()

        self._finished = True
        return Token(TokenType.EOF, "", self.line, self.column)

    def _read_identifier(self) -> Token:
        start_line = self.line
        start_col = self.column

        chars: list[str] = []

        while not self._eof():
            ch = self._peek()

            if ch.isspace():
                break

            if ch in "{}=":
                break

            chars.append(ch)
            self._advance()

        return Token(
            TokenType.IDENTIFIER,
            "".join(chars).strip(),
            start_line,
            start_col,
        )

    def _peek(self) -> str:
        return self.text[self.index]

    def _advance(self) -> None:
        self.index += 1
        self.column += 1

    def _advance_line(self) -> None:
        self.index += 1
        self.line += 1
        self.column = 1

    def _eof(self) -> bool:
        return self.index >= len(self.text)

    def _make(self, token_type: TokenType, value: str) -> Token:
        return Token(token_type, value, self.line, self.column)

    def _read_property_value(self) -> Token:
        start_line = self.line
        start_column = self.column

        # Skip the single space after '=' if present.
        if not self._eof() and self._peek() == " ":
            self._advance()

        chars: list[str] = []

        while not self._eof():
            ch = self._peek()

            if ch == "\n":
                break

            chars.append(ch)
            self._advance()

        return Token(
            TokenType.PROPERTY_VALUE,
            "".join(chars),
            start_line,
            start_column,
        )
