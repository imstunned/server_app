"""Роутеры приложения."""

from .authentication_router import authentication_router
from .authorization_router import authorization_router
from .post_router import post_router
from .user_router import user_router

__all__ = [
    'authentication_router',
    'authorization_router',
    'post_router',
    'user_router',
]
