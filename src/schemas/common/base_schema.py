"""Базовая схема приложения."""

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    """
    Базовая схема.
    """

    model_config = ConfigDict(
        extra='ignore',
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )
