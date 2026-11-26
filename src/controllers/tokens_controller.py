"""Контроллер для работы с токенами."""

from src.interfaces.controllers import BaseControllerInterface
from src.repositories import AccessTokenRepository
from src.repositories import RefreshTokenRepository
from src.repositories import UserRepository
from src.schemas.responses import TokensResponse
from src.utils import AccessTokenDtoMapper
from src.utils import CommonUtils
from src.utils import RefreshTokenDtoMapper
from src.utils import TokensResponseMapper


class TokensController(BaseControllerInterface):
    """
    Контроллер для работы с токенами.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        refresh_token_repository: RefreshTokenRepository,
        access_token_repository: AccessTokenRepository,
    ):
        self._user_repository = user_repository
        self._refresh_token_repository = refresh_token_repository
        self._access_token_repository = access_token_repository

    async def create_tokens(self, user_id: int) -> TokensResponse:
        """
        Создание новой пары токенов.

        :param user_id: ID пользователя.
        :return: Пара токенов.
        """

        refresh_token_full_dto = RefreshTokenDtoMapper.map_from_user_id(user_id=user_id)
        refresh_token_full_dto = await self._refresh_token_repository.upsert(dto=refresh_token_full_dto)

        access_token_full_dto = AccessTokenDtoMapper.map_from_refresh_token(
            user_id=user_id,
            refresh_token_dto=refresh_token_full_dto,
        )
        access_token_full_dto = await self._access_token_repository.upsert(dto=access_token_full_dto)

        await self._user_repository.update_last_login_at(user_id=user_id)

        return TokensResponseMapper.map_tokens_response(
            access_token=CommonUtils.create_jwt_token(token_dto=access_token_full_dto),
            refresh_token=CommonUtils.create_jwt_token(token_dto=refresh_token_full_dto),
        )
