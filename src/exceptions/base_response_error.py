"""Базовый класс ошибок ответов."""

from .base_custom_error import BaseCustomError


class BaseResponseError(BaseCustomError):
    """
    Базовый класс ошибок ответов.
    """

    def __init__(self, message: str, code: int):
        super().__init__(message=message)
        self._code = code

    @property
    def code(self) -> int:
        return self._code
