"""Зависимости репозиториев."""

from typing import Annotated
from typing import List

from fastapi import Depends

from src.repositories import PostRepository
from src.schemas.data_transfer_objects import PostFullDto
from .common_dependencies import get_posts


async def get_post_repository(posts: Annotated[List[PostFullDto], Depends(get_posts)]) -> PostRepository:
    """
    Зависимость для внедрения репозитория для работы с постами.

    :param posts: Список постов.
    :return: Репозиторий для работы с постами
    """

    return PostRepository(posts=posts)
