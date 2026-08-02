from kerbalforge.models import Token

from .source import SourceLocation, SourceSpan


class SourceSpanner:
    @staticmethod
    def location(line: int, column: int) -> SourceLocation:
        return SourceLocation(line, column)

    @staticmethod
    def locations(
        start: SourceLocation,
        end: SourceLocation,
    ) -> SourceSpan:
        return SourceSpan(start, end)

    @staticmethod
    def token(token: Token) -> SourceSpan:
        location = SourceSpanner.location(
            token.line,
            token.column,
        )

        return SourceSpan(location, location)

    @staticmethod
    def between(
        start: Token,
        end: Token,
    ) -> SourceSpan:
        return SourceSpan(
            SourceSpanner.location(
                start.line,
                start.column,
            ),
            SourceSpanner.location(
                end.line,
                end.column,
            ),
        )
