"""Базовый класс ошибок."""


class BaseCustomError(Exception):
    """
    Базовый класс ошибок.
    """

    def __init__(self, message: str):
        self._message = message

    @property
    def message(self) -> str:
        return self._message
