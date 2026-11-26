"""Репозиторий для работы с пользователями."""

from typing import Optional

from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import UserModel
from src.schemas.data_transfer_objects import UserFullDto
from src.schemas.data_transfer_objects import UserShortDto
from .base_db_repository import BaseDbRepository


class UserRepository(BaseDbRepository[UserModel, UserFullDto, UserShortDto]):
    """
    Репозиторий для работы с пользователями.
    """

    def __init__(
        self,
        async_db_session: AsyncSession,
    ):
        super().__init__(
            async_db_session=async_db_session,
            model_type=UserModel,
            full_schema_type=UserFullDto,
            short_schema_type=UserShortDto,
        )

    async def get_user_by_login(self, login: str) -> Optional[UserFullDto]:
        """
        Получение пользователя по логину.

        :param login: Логин пользователя.
        :return: Полный DTO пользователя.
        """

        statement = select(self.model_type).where(self.model_type.login == login)
        result = await self._async_db_session.execute(statement)
        model = result.scalar_one_or_none()

        if model:
            return self._full_schema_type.model_validate(obj=model)

        return None

    async def update_last_login_at(self, user_id: int) -> None:
        """
        Обновление даты последнего входа пользователя.

        :param user_id: ID пользователя.
        :return: None.
        """

        statement = (
            update(self.model_type)
            .where(self.model_type.id == user_id)
            .values(last_login_at=func.now())
        )
        await self._async_db_session.execute(statement)
