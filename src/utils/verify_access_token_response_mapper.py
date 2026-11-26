"""Маппер ответа на проверку access-токена."""

from src.schemas.responses import VerifyAccessTokenResponse


class VerifyAccessTokenResponseMapper:
    """
    Сборка ответа на проверку access-токена.
    """

    @staticmethod
    def map_verify_access_token_response(access_token: str) -> VerifyAccessTokenResponse:
        """
        Сборка схемы ответа на проверку access-токена.

        :param access_token: access-токен.
        :return: Ответ на проверку access-токена.
        """

        return VerifyAccessTokenResponse(access_token=access_token)
