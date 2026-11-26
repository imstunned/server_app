"""Зависимости контроллеров."""

from typing import Annotated

from fastapi import Depends
from passlib.context import CryptContext

from src.controllers import AuthenticationController
from src.controllers import AuthorizationController
from src.controllers import PostController
from src.controllers import TokensController
from src.controllers import UserController
from src.repositories import AccessTokenRepository
from src.repositories import PostRepository
from src.repositories import RefreshTokenRepository
from src.repositories import UserRepository
from .common_dependencies import get_password_context
from .repositories_dependencies import get_access_token_repository
from .repositories_dependencies import get_post_repository
from .repositories_dependencies import get_refresh_token_repository
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


async def get_tokens_controller(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    access_token_repository: Annotated[AccessTokenRepository, Depends(get_access_token_repository)],
    refresh_token_repository: Annotated[RefreshTokenRepository, Depends(get_refresh_token_repository)],
) -> TokensController:
    """
    Зависимость для внедрения контроллера для работы с токенами.

    :param user_repository: Репозиторий для работы с пользователями.
    :param access_token_repository: Репозиторий для работы с access-токенами.
    :param refresh_token_repository: Репозиторий для работы с refresh-токенами.
    :return: Контроллер для работы с токенами.
    """

    return TokensController(
        user_repository=user_repository,
        access_token_repository=access_token_repository,
        refresh_token_repository=refresh_token_repository,
    )


async def get_authorization_controller(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    access_token_repository: Annotated[AccessTokenRepository, Depends(get_access_token_repository)],
    refresh_token_repository: Annotated[RefreshTokenRepository, Depends(get_refresh_token_repository)],
    password_context: Annotated[CryptContext, Depends(get_password_context)],
) -> AuthorizationController:
    """
    Зависимость для внедрения контроллера авторизации.

    :param user_repository: Репозиторий для работы с пользователями.
    :param access_token_repository: Репозиторий для работы с access-токенами.
    :param refresh_token_repository: Репозиторий для работы с refresh-токенами.
    :param password_context: Контекст шифрования паролей.
    :return: Контроллер авторизации.
    """

    return AuthorizationController(
        user_repository=user_repository,
        access_token_repository=access_token_repository,
        refresh_token_repository=refresh_token_repository,
        password_context=password_context,
    )


async def get_authentication_controller(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    access_token_repository: Annotated[AccessTokenRepository, Depends(get_access_token_repository)],
    refresh_token_repository: Annotated[RefreshTokenRepository, Depends(get_refresh_token_repository)],
) -> AuthenticationController:
    """
    Зависимость для внедрения контроллера аутентификации.

    :param user_repository: Репозиторий для работы с пользователями.
    :param access_token_repository: Репозиторий для работы с access-токенами.
    :param refresh_token_repository: Репозиторий для работы с refresh-токенами.
    :return: Контроллер аутентификации.
    """

    return AuthenticationController(
        user_repository=user_repository,
        access_token_repository=access_token_repository,
        refresh_token_repository=refresh_token_repository,
    )
