"""Зависимости FastAPI."""

from .common_dependencies import get_password_context
from .common_dependencies import sqlalchemy_async_session_generator
from .controllers_dependencies import get_post_controller
from .controllers_dependencies import get_user_controller
from .repositories_dependencies import get_post_repository
from .repositories_dependencies import get_user_repository

__all__ = [
    'get_password_context',
    'get_post_controller',
    'get_post_repository',
    'get_user_controller',
    'get_user_repository',
    'sqlalchemy_async_session_generator',
]
