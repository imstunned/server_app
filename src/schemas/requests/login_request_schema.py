"""Запрос для входа в систему."""

from pydantic import Field

from src.schemas.common import BaseSchema


class LoginRequestSchema(BaseSchema):
    """
    Запрос для входа в систему.
    """

    login: str = Field(
        description='Логин пользователя',
        min_length=1,
        max_length=255,
        kw_only=True,
        examples=['login'],
    )
    password: str = Field(
        description='Пароль пользователя',
        min_length=1,
        max_length=255,
        kw_only=True,
        examples=['qwerty123'],
    )
