"""Ошибка невалидного JWT-токена."""

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class InvalidTokenError(BaseResponseError):
    """
    Ошибка невалидного JWT-токена.
    """

    def __init__(self):
        super().__init__(
            message=MessageEnum.INVALID_TOKEN_ERROR_MESSAGE,
            code=HTTPStatus.BAD_REQUEST,
        )
