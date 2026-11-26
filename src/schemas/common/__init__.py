"""Общие схемы приложения."""

from .base_schema import BaseSchema
from .mixin_id_schema import MixinIdSchema
from .mixin_soft_delete_schema import MixinSoftDeleteSchema

__all__ = [
    'BaseSchema',
    'MixinIdSchema',
    'MixinSoftDeleteSchema',
]
