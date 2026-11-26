"""DTO создания поста."""

from pydantic import Field

from src.schemas.common import BaseSchema


class PostCreateDto(BaseSchema):
    """
    DTO создания поста.
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
