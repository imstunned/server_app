"""Маппер ответа с токенами."""

from src.schemas.responses import TokensResponse


class TokensResponseMapper:
    """
    Сборка схемы ответа на создание/обновление токенов.
    """

    @staticmethod
    def map_tokens_response(access_token: str, refresh_token: str) -> TokensResponse:
        """
        Сборка схемы ответа на создание/обновление токенов.

        :param access_token: Токен доступа.
        :param refresh_token: Токен обновления.
        :return: Схема ответа на создание/обновление токенов.
        """

        return TokensResponse(access_token=access_token, refresh_token=refresh_token)
