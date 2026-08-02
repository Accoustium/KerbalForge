from kerbalforge.models import Token

from .source import SourceLocation, SourceSpan


class SourceSpanner:
    @staticmethod
    def location(line: int, column: int) -> SourceLocation:
        return SourceLocation(line, column)

    @staticmethod
    def token(token: Token) -> SourceSpan:
        return SourceSpan(
            SourceSpanner.location(token.line, token.column), SourceSpanner.location(token.line, token.column)
        )

    @staticmethod
    def between(
        start: Token,
        end: Token,
    ) -> SourceSpan:
        return SourceSpan(
            SourceSpanner.location(start.line, start.column), SourceSpanner.location(end.line, end.column)
        )
