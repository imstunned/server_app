"""Полный DTO поста."""

from datetime import datetime
from typing import Optional

from pydantic import Field

from src.schemas.common import MixinIdSchema
from src.schemas.common import MixinSoftDeleteSchema


class PostFullDto(MixinIdSchema, MixinSoftDeleteSchema):
    """
    Полный DTO поста.
    """

    author_id: int = Field(
        description='ID автора поста',
        ge=1,
        kw_only=True,
        examples=[1],
    )
    name: str = Field(
        description='Название поста',
        min_length=1,
        max_length=255,
        kw_only=True,
        examples=['Мой первый пост'],
    )
    content: str = Field(
        description='Текстовое содержание поста',
        min_length=1,
        kw_only=True,
        examples=['Post content'],
    )
    created_at: Optional[datetime] = Field(
        default=None,
        description='Дата и время создания поста',
        kw_only=True,
        examples=['2025-01-01T12:00:00'],
    )
