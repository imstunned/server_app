"""Модель поста."""

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy import Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings
from .mixin_auto_id_model import MixinAutoIdModel
from .mixin_soft_delete_model import MixinSoftDeleteModel
from .user_model import UserModel


class PostModel(MixinAutoIdModel, MixinSoftDeleteModel):
    """
    Модель постов.
    """

    __abstract__ = False
    __tablename__ = 'post'
    __table_args__ = {
        'schema': app_settings.POSTS_SQL_SCHEMA,
    }

    author_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(UserModel.id, ondelete='CASCADE'),
        nullable=False,
        comment='ID автора поста',
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment='Название поста',
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        comment='Контент',
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(),
        nullable=False,
        server_default=func.now(),
        comment='Создан',
    )
