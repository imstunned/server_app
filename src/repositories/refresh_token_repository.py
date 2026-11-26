"""Репозиторий для работы с refresh-токенами."""

from datetime import datetime

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import RefreshTokenModel
from src.schemas.data_transfer_objects import RefreshTokenFullDto
from src.schemas.responses import DeleteExpiredTokensResponse
from src.utils import DeleteExpiredTokensResponseMapper
from .base_db_repository import BaseDbRepository


class RefreshTokenRepository(BaseDbRepository[RefreshTokenModel, RefreshTokenFullDto, RefreshTokenFullDto]):
    """
    Репозиторий для работы с refresh-токенами.
    """

    def __init__(
        self,
        async_db_session: AsyncSession,
    ):
        super().__init__(
            async_db_session=async_db_session,
            model_type=RefreshTokenModel,
            full_schema_type=RefreshTokenFullDto,
            short_schema_type=RefreshTokenFullDto,
        )

    async def delete_expired_tokens(self) -> DeleteExpiredTokensResponse:
        """
        Удаление refresh-токенов, которые не актуальны.

        :return: Ответ с количеством удалённых refresh-токенов.
        """

        statement = delete(self.model_type).where(
            self.model_type.expire_at < datetime.now(),
        )
        result = await self._async_db_session.execute(statement=statement)

        return DeleteExpiredTokensResponseMapper.map_delete_expired_tokens_response(
            deleted_tokens_count=result.rowcount,
        )
