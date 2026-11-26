"""DTO частичного обновления пользователя."""

from typing import Optional

from pydantic import Field

from src.schemas.common import BaseSchema


class UserUpdateDto(BaseSchema):
    """
    DTO частичного обновления пользователя.
    """

    username: Optional[str] = Field(
        default=None,
        description='Никнейм',
        min_length=1,
        max_length=50,
        kw_only=True,
        examples=['Username'],
    )
    email: Optional[str] = Field(
        default=None,
        description='Почта',
        min_length=1,
        max_length=120,
        kw_only=True,
        examples=['example@mail.com'],
    )
    login: Optional[str] = Field(
        default=None,
        description='Логин',
        min_length=1,
        max_length=255,
        kw_only=True,
        examples=['login'],
    )
    password: Optional[str] = Field(
        default=None,
        description='Пароль в открытом виде',
        min_length=8,
        max_length=255,
        kw_only=True,
        examples=['qwerty123'],
    )
