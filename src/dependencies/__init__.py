"""Зависимости FastAPI."""

from .common_dependencies import get_posts
from .controllers_dependencies import get_post_controller
from .repositories_dependencies import get_post_repository

__all__ = [
    'get_posts',
    'get_post_controller',
    'get_post_repository',
]
