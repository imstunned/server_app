"""DTO для частичного обновления поста."""

from typing import Optional

from pydantic import Field

from src.schemas.common import BaseSchema


class PostUpdateDto(BaseSchema):
    """
    DTO частичного обновления поста.
    """

    author_name: Optional[str] = Field(
        default=None,
        description='Имя автора поста',
        min_length=1,
        max_length=255,
        kw_only=True,
        examples=['Author'],
    )
    content: Optional[str] = Field(
        default=None,
        description='Текстовое содержание поста',
        min_length=1,
        kw_only=True,
        examples=['Post content'],
    )
