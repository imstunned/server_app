"""Репозиторий для работы с access-токенами."""

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import AccessTokenModel
from src.schemas.data_transfer_objects import AccessTokenFullDto
from .base_db_repository import BaseDbRepository


class AccessTokenRepository(BaseDbRepository[AccessTokenModel, AccessTokenFullDto, AccessTokenFullDto]):
    """
    Репозиторий для работы с access-токенами.
    """

    def __init__(
        self,
        async_db_session: AsyncSession,
    ):
        super().__init__(
            async_db_session=async_db_session,
            model_type=AccessTokenModel,
            full_schema_type=AccessTokenFullDto,
            short_schema_type=AccessTokenFullDto,
        )
