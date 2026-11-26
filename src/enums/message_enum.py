"""Перечисление сообщений."""

from enum import Enum


class MessageEnum(str, Enum):
    """
    Перечисление сообщений.
    """

    INVALID_ACCESS_TOKEN_ERROR_MESSAGE = 'Недействительный токен доступа'
    INVALID_REFRESH_TOKEN_ERROR_MESSAGE = 'Недействительный refresh-токен'
    INVALID_CREDENTIALS_ERROR_MESSAGE = 'Недействительные учётные данные'
    INVALID_TOKEN_ERROR_MESSAGE = 'Недействительный токен'
    EXPIRED_JWT_TOKEN_ERROR_MESSAGE = 'Срок действия jwt-токена истёк'
