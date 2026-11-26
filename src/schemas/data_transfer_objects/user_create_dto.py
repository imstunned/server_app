"""DTO создания пользователя."""

from pydantic import Field

from src.schemas.common import BaseSchema


class UserCreateDto(BaseSchema):
    """
    DTO создания пользователя.
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
    password: str = Field(
        description='Пароль в открытом виде',
        min_length=8,
        max_length=255,
        kw_only=True,
        examples=['qwerty123'],
    )
