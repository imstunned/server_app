"""Ответ на запрос удаления неактуальных refresh-токенов."""

from pydantic import Field

from src.schemas.common import BaseSchema


class DeleteExpiredTokensResponse(BaseSchema):
    """
    Ответ на запрос удаления всех неактуальных refresh-токенов.
    """

    deleted_tokens_count: int = Field(
        description='Количество удаленных refresh-токенов',
        kw_only=True,
        examples=[1],
    )
