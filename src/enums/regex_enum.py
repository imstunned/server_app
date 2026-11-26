"""Перечисление регулярных выражений."""

from enum import Enum


class RegexEnum(str, Enum):
    """
    Перечисление регулярных выражений.
    """

    JWT_TOKEN = r'^[\w-]+\.[\w-]+\.[\w-]+$'
