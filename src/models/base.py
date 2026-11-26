"""Базовая модель для ORM."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Базовая модель для ORM.
    """

    __abstract__ = True
