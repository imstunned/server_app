"""Маппер декодированного JWT-токена."""

from datetime import datetime
from typing import Any
from typing import Dict

from src.schemas.data_transfer_objects import TokenDto


class TokenDtoMapper:
    """
    Сборка сокращённой модели токена.
    """

    @staticmethod
    def get_from_decoded_dict(decoded_dict: Dict[str, Any]) -> TokenDto:
        """
        Маппинг сокращённой модели токена из декодированного словаря.

        :param decoded_dict: Декодированное тело токена.
        :return: Сокращённая модель токена.
        :raises KeyError: Если необходимые для сборки ключи отсутствуют в словаре.
        """

        return TokenDto(
            id=int(decoded_dict['jti']),
            user_id=int(decoded_dict['user']),
            expire_at=datetime.fromtimestamp(decoded_dict['exp']),
            created_at=datetime.fromtimestamp(decoded_dict['iat']),
        )
