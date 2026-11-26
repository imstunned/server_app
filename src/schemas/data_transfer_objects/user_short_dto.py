"""Краткий DTO пользователя (без пароля)."""

from datetime import datetime
from typing import Optional

from pydantic import Field

from src.schemas.common import MixinIdSchema
from src.schemas.common import MixinSoftDeleteSchema


class UserShortDto(MixinIdSchema, MixinSoftDeleteSchema):
    """
    Краткий DTO пользователя.
    """

    username: str = Field(
        description='Никнейм',
        min_length=1,
        max_length=50,
        kw_only=True,
        examples=['Username'],
    )
    email: str = Field(
        description='Почта',
        min_length=1,
        max_length=120,
        kw_only=True,
        examples=['example@mail.com'],
    )
    login: str = Field(
        description='Логин',
        min_length=1,
        max_length=255,
        kw_only=True,
        examples=['login'],
    )
    last_login_at: Optional[datetime] = Field(
        default=None,
        description='Дата последнего входа',
        kw_only=True,
        examples=['2025-01-01T12:00:00'],
    )
