"""Маппер DTO access-токена."""

from datetime import datetime
from datetime import timedelta

from settings import app_settings
from src.schemas.data_transfer_objects import AccessTokenFullDto
from src.schemas.data_transfer_objects import RefreshTokenFullDto


class AccessTokenDtoMapper:
    """
    Сборка DTO access-токенов.
    """

    @staticmethod
    def map_from_refresh_token(user_id: int, refresh_token_dto: RefreshTokenFullDto) -> AccessTokenFullDto:
        """
        Сборка access-токена, используя refresh-токен.

        :param user_id: ID пользователя.
        :param refresh_token_dto: DTO refresh-токена.
        :return: DTO access-токена.
        """

        now = datetime.now().replace(microsecond=0)

        return AccessTokenFullDto(
            user_id=user_id,
            expire_at=now + timedelta(minutes=app_settings.ACCESS_TOKEN_EXPIRES_MINUTES),
            created_at=now,
            refresh_id=refresh_token_dto.id,
        )
