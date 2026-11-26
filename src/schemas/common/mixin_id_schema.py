"""Схема с идентификатором."""

from typing import Optional

from pydantic import Field

from .base_schema import BaseSchema


class MixinIdSchema(BaseSchema):
    """
    Схема с идентификатором.
    """

    id: Optional[int] = Field(
        default=None,
        description='Идентификатор',
        ge=1,
        kw_only=True,
        examples=[1],
    )
