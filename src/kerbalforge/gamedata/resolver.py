from kerbalforge.ast import Document, required_property

from .models import PartDefinition


class PartResolver:
    def resolve(
        self,
        document: Document,
    ) -> PartDefinition:
        part = document.body[0]

        return PartDefinition(
            name=required_property(part, "name").value,  # type: ignore[arg-type]
            title=required_property(part, "title").value,  # type: ignore[arg-type]
            document=document,
        )
