"""Зависимости контроллеров."""

from typing import Annotated

from fastapi import Depends

from src.controllers import PostController
from src.repositories import PostRepository
from .repositories_dependencies import get_post_repository


async def get_post_controller(
    post_repository: Annotated[PostRepository, Depends(get_post_repository)],
) -> PostController:
    """
    Зависимость для внедрения контроллера для работы с постами.

    :param post_repository: Репозиторий для работы с постами.
    :return: Контроллер для работы с постами.
    """

    return PostController(post_repository=post_repository)
