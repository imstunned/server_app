"""Общие зависимости приложения."""

from typing import List

from src.schemas.data_transfer_objects import PostFullDto

posts: List[PostFullDto] = [
    PostFullDto(id=1, author_name='Bob', content='52'),
    PostFullDto(id=2, author_name='Billy', content='67'),
    PostFullDto(id=3, author_name='John', content='Lorem ipsum'),
]


async def get_posts() -> List[PostFullDto]:
    """
    Получение списка полных DTO постов.

    :return: Список полных DTO постов.
    """

    return posts
