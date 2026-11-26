"""Модель access-токена."""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings
from .mixin_auto_id_model import MixinAutoIdModel
from .refresh_token_model import RefreshTokenModel
from .user_model import UserModel


class AccessTokenModel(MixinAutoIdModel):
    """
    Модель access-токена.
    """

    __abstract__ = False
    __tablename__ = 'access_token'
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
        comment='Срок действия access-токена',
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        server_default=func.now(),
        nullable=False,
        comment='Дата создания access-токена',
    )
    refresh_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(RefreshTokenModel.id, ondelete='CASCADE'),
        nullable=False,
        comment='ID refresh-токена',
    )
