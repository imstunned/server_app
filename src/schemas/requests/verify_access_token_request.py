"""Запрос для проверки access-токена."""

from pydantic import Field

from src.enums import RegexEnum
from src.schemas.common import BaseSchema


class VerifyAccessTokenRequest(BaseSchema):
    """
    Запрос для проверки токена.
    """

    access_token: str = Field(
        pattern=RegexEnum.JWT_TOKEN.value,
        description='access-токен',
        kw_only=True,
        examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp'],
    )
