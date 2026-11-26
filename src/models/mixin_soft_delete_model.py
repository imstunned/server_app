"""Миксин для добавления полей метаданных удаления."""

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import expression

from .base import Base


class MixinSoftDeleteModel(Base):
    """
    Миксина для добавления полей метаданных удаления.
    """

    __abstract__ = True

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default=expression.false(),
        comment='Удалено',
    )
    deleted_by: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        default=None,
        server_default=expression.null(),
        comment='Удалил',
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(),
        nullable=True,
        default=None,
        server_default=expression.null(),
        comment='Время удаления',
    )
