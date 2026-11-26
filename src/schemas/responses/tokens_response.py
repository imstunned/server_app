"""Ответ на создание/обновление токенов."""

from pydantic import Field

from src.enums import RegexEnum
from src.schemas.common import BaseSchema


class TokensResponse(BaseSchema):
    """
    Ответ на создание/обновление токенов.
    """

    access_token: str = Field(
        description='Токен доступа',
        pattern=RegexEnum.JWT_TOKEN.value,
        examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp'],
    )
    refresh_token: str = Field(
        description='Токен обновления',
        pattern=RegexEnum.JWT_TOKEN.value,
        examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp'],
    )
