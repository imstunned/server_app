"""Полный DTO поста."""

from typing import Optional

from pydantic import Field

from src.schemas.common import BaseSchema


class PostFullDto(BaseSchema):
    """
    Полный DTO постов.
    """

    id: Optional[int] = Field(
        description='ID поста',
        default=None,
        ge=1,
        kw_only=True,
        examples=[1],
    )
    author_name: str = Field(
        description='Имя автора поста',
        kw_only=True,
        examples=['Author'],
    )
    content: str = Field(
        description='Текстовое содержание поста',
        kw_only=True,
        examples=['Post content'],
    )
