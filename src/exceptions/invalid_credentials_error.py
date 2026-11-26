"""Ошибка недействительных учётных данных."""

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class InvalidCredentialsError(BaseResponseError):
    """
    Исключение, возникающее при неправильной аутентификации пользователя.
    """

    def __init__(self):
        super().__init__(
            message=MessageEnum.INVALID_CREDENTIALS_ERROR_MESSAGE,
            code=HTTPStatus.BAD_REQUEST,
        )
