"""Схема с полями метаданных удаления."""

from datetime import datetime
from typing import Optional

from pydantic import Field

from .base_schema import BaseSchema


class MixinSoftDeleteSchema(BaseSchema):
    """
    Схема с полями метаданных удаления.
    """

    is_deleted: bool = Field(
        default=False,
        description='Удалено',
        kw_only=True,
    )
    deleted_by: Optional[int] = Field(
        default=None,
        description='Кем удалено',
        kw_only=True,
    )
    deleted_at: Optional[datetime] = Field(
        default=None,
        description='Время удаления',
        kw_only=True,
    )
