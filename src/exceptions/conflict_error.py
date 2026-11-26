"""Ошибка конфликта данных (нарушение уникальности)."""

from http import HTTPStatus

from .base_response_error import BaseResponseError


class ConflictError(BaseResponseError):
    """
    Ошибка конфликта данных.
    """

    def __init__(self, message: str):
        super().__init__(message=message, code=HTTPStatus.CONFLICT)
