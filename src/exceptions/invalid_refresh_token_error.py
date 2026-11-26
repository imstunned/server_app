"""Ошибка невалидного refresh-токена."""

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class InvalidRefreshTokenError(BaseResponseError):
    """
    Ошибка невалидного refresh-токена.
    """

    def __init__(self):
        super().__init__(
            message=MessageEnum.INVALID_REFRESH_TOKEN_ERROR_MESSAGE,
            code=HTTPStatus.FORBIDDEN,
        )
