"""Зависимости репозиториев."""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories import AccessTokenRepository
from src.repositories import PostRepository
from src.repositories import RefreshTokenRepository
from src.repositories import UserRepository
from .common_dependencies import sqlalchemy_async_session_generator


async def get_post_repository(
    async_db_session: Annotated[AsyncSession, Depends(sqlalchemy_async_session_generator)],
) -> PostRepository:
    """
    Зависимость для внедрения репозитория для работы с постами.

    :param async_db_session: Асинхронная сессия БД.
    :return: Репозиторий для работы с постами
    """

    return PostRepository(async_db_session=async_db_session)


async def get_user_repository(
    async_db_session: Annotated[AsyncSession, Depends(sqlalchemy_async_session_generator)],
) -> UserRepository:
    """
    Зависимость для внедрения репозитория для работы с пользователями.

    :param async_db_session: Асинхронная сессия БД.
    :return: Репозиторий для работы с пользователями.
    """

    return UserRepository(async_db_session=async_db_session)


async def get_access_token_repository(
    async_db_session: Annotated[AsyncSession, Depends(sqlalchemy_async_session_generator)],
) -> AccessTokenRepository:
    """
    Зависимость для внедрения репозитория для работы с access-токенами.

    :param async_db_session: Асинхронная сессия БД.
    :return: Репозиторий для работы с access-токенами.
    """

    return AccessTokenRepository(async_db_session=async_db_session)


async def get_refresh_token_repository(
    async_db_session: Annotated[AsyncSession, Depends(sqlalchemy_async_session_generator)],
) -> RefreshTokenRepository:
    """
    Зависимость для внедрения репозитория для работы с refresh-токенами.

    :param async_db_session: Асинхронная сессия БД.
    :return: Репозиторий для работы с refresh-токенами.
    """

    return RefreshTokenRepository(async_db_session=async_db_session)
