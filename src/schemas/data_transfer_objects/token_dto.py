"""DTO декодированного JWT-токена."""

from datetime import datetime

from pydantic import Field

from src.schemas.common import MixinIdSchema


class TokenDto(MixinIdSchema):
    """
    DTO токена.
    """

    user_id: int = Field(
        ge=1,
        description='Идентификатор пользователя',
        kw_only=True,
        examples=[1],
    )
    expire_at: datetime = Field(
        description='Срок действия токена',
        kw_only=True,
        examples=['2025-01-01T12:15:00'],
    )
    created_at: datetime = Field(
        description='Дата и время создания токена',
        kw_only=True,
        examples=['2025-01-01T12:00:00'],
    )
