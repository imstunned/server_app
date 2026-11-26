"""DTO (Data Transfer Object) приложения."""

from .post_create_dto import PostCreateDto
from .post_full_dto import PostFullDto
from .post_short_dto import PostShortDto
from .post_update_dto import PostUpdateDto
from .user_create_dto import UserCreateDto
from .user_full_dto import UserFullDto
from .user_short_dto import UserShortDto
from .user_update_dto import UserUpdateDto

__all__ = [
    'PostCreateDto',
    'PostFullDto',
    'PostShortDto',
    'PostUpdateDto',
    'UserCreateDto',
    'UserFullDto',
    'UserShortDto',
    'UserUpdateDto',
]
