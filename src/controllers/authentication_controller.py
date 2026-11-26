"""Контроллер для аутентификации пользователя."""

from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from src.exceptions import ExpiredJwtTokenError
from src.exceptions import InvalidAccessTokenError
from src.exceptions import InvalidRefreshTokenError
from src.exceptions import InvalidTokenError
from src.repositories import AccessTokenRepository
from src.repositories import RefreshTokenRepository
from src.repositories import UserRepository
from src.schemas.data_transfer_objects import AccessTokenFullDto
from src.schemas.data_transfer_objects import RefreshTokenFullDto
from src.schemas.data_transfer_objects import TokenDto
from src.schemas.requests import RefreshTokenRequest
from src.schemas.requests import VerifyAccessTokenRequest
from src.schemas.responses import DeleteExpiredTokensResponse
from src.schemas.responses import TokensResponse
from src.schemas.responses import VerifyAccessTokenResponse
from src.utils import CommonUtils
from src.utils import VerifyAccessTokenResponseMapper
from .tokens_controller import TokensController


class AuthenticationController(TokensController):
    """
    Контроллер для аутентификации пользователя.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        access_token_repository: AccessTokenRepository,
        refresh_token_repository: RefreshTokenRepository,
    ):
        super().__init__(
            user_repository=user_repository,
            refresh_token_repository=refresh_token_repository,
            access_token_repository=access_token_repository,
        )

    async def _check_token(self, token_dto: TokenDto, is_refresh: bool = False) -> bool:
        """
        Проверка корректности токена.

        :param token_dto: Краткая информация о токене.
        :param is_refresh: Флаг для определения типа токена.
        :return: Признак корректности токена.
        """

        token_dto_from_db: Optional[Union[AccessTokenFullDto, RefreshTokenFullDto]]

        if is_refresh:
            token_dto_from_db = await self._refresh_token_repository.get_one_full_by_id(
                object_id=token_dto.id,  # type: ignore[arg-type]
            )
        else:
            token_dto_from_db = await self._access_token_repository.get_one_full_by_id(
                object_id=token_dto.id,  # type: ignore[arg-type]
            )

        if token_dto_from_db is None:
            return False

        return bool(
            token_dto_from_db.user_id == token_dto.user_id
            and token_dto_from_db.created_at == token_dto.created_at
            and token_dto_from_db.expire_at == token_dto.expire_at
        )

    async def logout_user(self, refresh_token_request: RefreshTokenRequest) -> Dict[str, Any]:
        """
        Выход пользователя из приложения.

        :param refresh_token_request: Данные для проверки refresh токена.
        :return: Пустой словарь при успешном выходе.
        :raise InvalidRefreshTokenError: Если refresh-токен невалиден.
        """

        token_dto = CommonUtils.decode_jwt_token(token=refresh_token_request.refresh_token)

        if await self._check_token(token_dto=token_dto, is_refresh=True):
            await self._refresh_token_repository.delete_one_by_id(
                object_id=token_dto.id,  # type: ignore[arg-type]
            )

            return dict()

        raise InvalidRefreshTokenError()

    async def verify_access_token(
        self,
        verify_access_token_request: VerifyAccessTokenRequest,
    ) -> VerifyAccessTokenResponse:
        """
        Проверка access токена.

        :param verify_access_token_request: Данные для проверки access токена.
        :return: При успешной проверке возвращается текущий access токен.
        :raise InvalidAccessTokenError: Если access токен невалиден.
        """

        token_dto: Optional[TokenDto] = None

        try:
            token_dto = CommonUtils.decode_jwt_token(token=verify_access_token_request.access_token)
        except (ExpiredJwtTokenError, InvalidTokenError) as exc:
            print(f'Error decode access token: {exc}')

        if token_dto:
            if await self._check_token(token_dto=token_dto):
                user_dto = await self._user_repository.get_one_full_by_id(object_id=token_dto.user_id)

                if user_dto:
                    if not user_dto.is_deleted:
                        return VerifyAccessTokenResponseMapper.map_verify_access_token_response(
                            access_token=verify_access_token_request.access_token,
                        )

        raise InvalidAccessTokenError()

    async def refresh_tokens(self, refresh_token_request: RefreshTokenRequest) -> TokensResponse:
        """
        Проверка refresh токена и создание новой пары токенов.

        :param refresh_token_request: Данные для проверки refresh токена.
        :return: Новая пара токенов.
        :raise InvalidRefreshTokenError: Если refresh токен невалиден.
        """

        token_dto: Optional[TokenDto] = None

        try:
            token_dto = CommonUtils.decode_jwt_token(token=refresh_token_request.refresh_token)
        except (ExpiredJwtTokenError, InvalidTokenError) as exc:
            print(f'Error decode refresh token: {exc}')

        if token_dto:
            if await self._check_token(token_dto=token_dto, is_refresh=True):
                user_dto = await self._user_repository.get_one_full_by_id(object_id=token_dto.user_id)

                if user_dto:
                    if not user_dto.is_deleted:
                        await self._refresh_token_repository.delete_one_by_id(object_id=token_dto.id)

                        return await self.create_tokens(user_id=user_dto.id)

        raise InvalidRefreshTokenError()

    async def delete_expired_tokens(self) -> DeleteExpiredTokensResponse:
        """
        Удаление просроченных токенов.

        :return: Ответ с количеством удалённых refresh-токенов.
        """

        return await self._refresh_token_repository.delete_expired_tokens()
