"""Кастомные ошибки приложения."""

from .base_custom_error import BaseCustomError
from .base_response_error import BaseResponseError
from .conflict_error import ConflictError
from .handlers import register_exception_handlers

__all__ = [
    'BaseCustomError',
    'BaseResponseError',
    'ConflictError',
    'register_exception_handlers',
]
