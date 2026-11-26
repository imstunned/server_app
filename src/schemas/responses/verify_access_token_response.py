"""Ответ на проверку access-токена."""

from pydantic import Field

from src.enums import RegexEnum
from src.schemas.common import BaseSchema


class VerifyAccessTokenResponse(BaseSchema):
    """
    Ответ на проверку access-токена.
    """

    access_token: str = Field(
        description='Токен доступа',
        pattern=RegexEnum.JWT_TOKEN.value,
        examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp'],
    )
