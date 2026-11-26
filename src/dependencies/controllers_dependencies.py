"""Зависимости контроллеров."""

from typing import Annotated

from fastapi import Depends
from passlib.context import CryptContext

from src.controllers import PostController
from src.controllers import UserController
from src.repositories import PostRepository
from src.repositories import UserRepository
from .common_dependencies import get_password_context
from .repositories_dependencies import get_post_repository
from .repositories_dependencies import get_user_repository


async def get_post_controller(
    post_repository: Annotated[PostRepository, Depends(get_post_repository)],
) -> PostController:
    """
    Зависимость для внедрения контроллера для работы с постами.

    :param post_repository: Репозиторий для работы с постами.
    :return: Контроллер для работы с постами.
    """

    return PostController(post_repository=post_repository)


async def get_user_controller(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    password_context: Annotated[CryptContext, Depends(get_password_context)],
) -> UserController:
    """
    Зависимость для внедрения контроллера для работы с пользователями.

    :param user_repository: Репозиторий для работы с пользователями.
    :param password_context: Контекст шифрования паролей.
    :return: Контроллер для работы с пользователями.
    """

    return UserController(
        user_repository=user_repository,
        password_context=password_context,
    )
