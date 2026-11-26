"""Модель refresh-токена."""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings
from .mixin_auto_id_model import MixinAutoIdModel
from .user_model import UserModel


class RefreshTokenModel(MixinAutoIdModel):
    """
    Модель refresh-токена.
    """

    __abstract__ = False
    __tablename__ = 'refresh_token'
    __table_args__ = {
        'schema': app_settings.USERS_SQL_SCHEMA,
    }

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(UserModel.id, ondelete='CASCADE'),
        nullable=False,
        comment='ID пользователя',
    )
    expire_at: Mapped[datetime] = mapped_column(
        DateTime(),
        nullable=False,
        comment='Дата истечения refresh-токена',
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        server_default=func.now(),
        nullable=False,
        comment='Дата создания refresh-токена',
    )
