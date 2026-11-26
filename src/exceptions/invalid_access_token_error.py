"""Ошибка невалидного access-токена."""

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class InvalidAccessTokenError(BaseResponseError):
    """
    Ошибка невалидного access-токена.
    """

    def __init__(self):
        super().__init__(
            message=MessageEnum.INVALID_ACCESS_TOKEN_ERROR_MESSAGE,
            code=HTTPStatus.UNAUTHORIZED,
        )
