"""Краткий DTO поста."""

from datetime import datetime

from pydantic import Field

from src.schemas.common import MixinIdSchema


class PostShortDto(MixinIdSchema):
    """
    Краткий DTO поста.
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
    created_at: datetime = Field(
        description='Дата и время создания поста',
        kw_only=True,
        examples=['2025-01-01T12:00:00'],
    )
