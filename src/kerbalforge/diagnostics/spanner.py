from kerbalforge.models import Token

from .source import SourceLocation, SourceSpan


class SourceSpanner:
    @staticmethod
    def single(location: Token | SourceLocation) -> SourceSpan:
        return SourceSpan(location, location)

    @staticmethod
    def between(
        start: Token | SourceLocation,
        end: Token | SourceLocation,
    ) -> SourceSpan:
        return SourceSpan(start, end)
