from __future__ import annotations

from .tokens import Token, TokenType


class Tokenizer:

    def __init__(self, text: str):
        self.text = text
        self.index = 0
        self.line = 1
        self.column = 1

    def __iter__(self):
        return self

    def __next__(self):
        ...
    
    def tokenize(self) -> list[Token]:
        # return list(self)

        tokens: list[Token] = []

        while not self._eof():

            ch = self._peek()

            if ch in " \t\r":
                self._advance()
                continue

            if ch == "\n":
                self._advance_line()
                continue

            if ch == "{":
                tokens.append(self._make(TokenType.LBRACE, "{"))
                self._advance()
                continue

            if ch == "}":
                tokens.append(self._make(TokenType.RBRACE, "}"))
                self._advance()
                continue

            if ch == "=":
                tokens.append(self._make(TokenType.EQUALS, "="))
                self._advance()
                continue

            tokens.append(self._identifier())

        tokens.append(Token(TokenType.EOF, "", self.line, self.column))

        return tokens

    def _identifier(self) -> Token:

        start_line = self.line
        start_col = self.column

        chars = []

        while not self._eof():

            ch = self._peek()

            if ch in "\n={}":
                break

            chars.append(ch)

            self._advance()

        return Token(
            TokenType.IDENTIFIER,
            "".join(chars).strip(),
            start_line,
            start_col,
        )

    def _peek(self):
        return self.text[self.index]

    def _advance(self):
        self.index += 1
        self.column += 1

    def _advance_line(self):
        self.index += 1
        self.line += 1
        self.column = 1

    def _eof(self):
        return self.index >= len(self.text)

    def _make(self, t, value):
        return Token(t, value, self.line, self.column)
