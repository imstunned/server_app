"""Фабрики зависимостей."""

from typing import AsyncGenerator
from typing import Callable

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker


def get_sqlalchemy_async_session_generator(
    async_session_maker: async_sessionmaker[AsyncSession],
) -> Callable[[], AsyncGenerator[AsyncSession, None]]:
    """
    Фабрика генератора асинхронных сессий БД.

    :param async_session_maker: Фабрика сессий.
    :return: Генератор асинхронных сессий.
    """

    async def sqlalchemy_async_session_generator() -> AsyncGenerator[AsyncSession, None]:
        """
        Генератор асинхронных сессий БД.

        :return: AsyncSession.
        """

        async_session = async_session_maker()

        try:
            yield async_session

            await async_session.commit()
        except SQLAlchemyError:
            await async_session.rollback()
            await async_session.close()

            raise
        else:
            await async_session.close()

    return sqlalchemy_async_session_generator
