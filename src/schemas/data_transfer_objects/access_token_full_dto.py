"""DTO access-токена."""

from datetime import datetime

from pydantic import Field

from src.schemas.common import MixinIdSchema


class AccessTokenFullDto(MixinIdSchema):
    """
    DTO access-токена.
    """

    user_id: int = Field(
        description='ID пользователя',
        ge=1,
        kw_only=True,
        examples=[1],
    )
    expire_at: datetime = Field(
        description='Срок действия токена',
        kw_only=True,
        examples=['2025-01-01T12:15:00'],
    )
    created_at: datetime = Field(
        description='Время создания токена',
        kw_only=True,
        examples=['2025-01-01T12:00:00'],
    )
    refresh_id: int = Field(
        ge=1,
        description='ID refresh-токена',
        kw_only=True,
        examples=[1],
    )
