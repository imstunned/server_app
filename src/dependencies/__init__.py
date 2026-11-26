"""Зависимости FastAPI."""

from .common_dependencies import get_password_context
from .common_dependencies import sqlalchemy_async_session_generator
from .controllers_dependencies import get_authentication_controller
from .controllers_dependencies import get_authorization_controller
from .controllers_dependencies import get_post_controller
from .controllers_dependencies import get_tokens_controller
from .controllers_dependencies import get_user_controller
from .repositories_dependencies import get_access_token_repository
from .repositories_dependencies import get_post_repository
from .repositories_dependencies import get_refresh_token_repository
from .repositories_dependencies import get_user_repository

__all__ = [
    'get_access_token_repository',
    'get_authentication_controller',
    'get_authorization_controller',
    'get_password_context',
    'get_post_controller',
    'get_post_repository',
    'get_refresh_token_repository',
    'get_tokens_controller',
    'get_user_controller',
    'get_user_repository',
    'sqlalchemy_async_session_generator',
]
