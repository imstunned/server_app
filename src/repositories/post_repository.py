"""Репозиторий для работы с постами."""

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import PostModel
from src.schemas.data_transfer_objects import PostFullDto
from src.schemas.data_transfer_objects import PostShortDto
from .base_db_repository import BaseDbRepository


class PostRepository(BaseDbRepository[PostModel, PostFullDto, PostShortDto]):
    """
    Репозиторий для работы с постами.
    """

    def __init__(
        self,
        async_db_session: AsyncSession,
    ):
        super().__init__(
            async_db_session=async_db_session,
            model_type=PostModel,
            full_schema_type=PostFullDto,
            short_schema_type=PostShortDto,
        )
