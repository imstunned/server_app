"""Ошибка истечения срока действия JWT-токена."""

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class ExpiredJwtTokenError(BaseResponseError):
    """
    Ошибка истечения срока действия access/refresh токена.
    """

    def __init__(self):
        super().__init__(
            message=MessageEnum.EXPIRED_JWT_TOKEN_ERROR_MESSAGE,
            code=HTTPStatus.BAD_REQUEST,
        )
