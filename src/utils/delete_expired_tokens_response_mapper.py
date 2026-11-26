"""Маппер ответа на удаление неактуальных refresh-токенов."""

from src.schemas.responses import DeleteExpiredTokensResponse


class DeleteExpiredTokensResponseMapper:
    """
    Маппер для ответа на запрос удаления всех неактуальных refresh-токенов.
    """

    @staticmethod
    def map_delete_expired_tokens_response(deleted_tokens_count: int) -> DeleteExpiredTokensResponse:
        """
        Сборка ответа на запрос удаления всех неактуальных refresh-токенов.

        :param deleted_tokens_count: Количество удалённых токенов.
        :return: Ответ на запрос удаления всех неактуальных refresh-токенов.
        """

        return DeleteExpiredTokensResponse(deleted_tokens_count=deleted_tokens_count)
