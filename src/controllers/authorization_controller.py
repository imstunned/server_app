"""Контроллер для авторизации пользователя."""

from passlib.context import CryptContext

from src.exceptions import InvalidCredentialsError
from src.repositories import AccessTokenRepository
from src.repositories import RefreshTokenRepository
from src.repositories import UserRepository
from src.schemas.requests import LoginRequestSchema
from src.schemas.responses import TokensResponse
from src.utils import CommonUtils
from .tokens_controller import TokensController


class AuthorizationController(TokensController):
    """
    Контроллер для авторизации пользователя.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        access_token_repository: AccessTokenRepository,
        refresh_token_repository: RefreshTokenRepository,
        password_context: CryptContext,
    ):
        super().__init__(
            user_repository=user_repository,
            refresh_token_repository=refresh_token_repository,
            access_token_repository=access_token_repository,
        )
        self._password_context = password_context

    async def login_user(self, login_request: LoginRequestSchema) -> TokensResponse:
        """
        Вход пользователя в приложение.

        :param login_request: Данные для входа пользователя.
        :return: При успешном входе возвращается пара токенов.
        :raise InvalidCredentialsError: Если логин или пароль неверны.
        """

        user_dto = await self._user_repository.get_user_by_login(login=login_request.login)

        if user_dto:
            is_valid_password = CommonUtils.verify_password(
                plain_password=login_request.password,
                hashed_password=user_dto.password,
                password_context=self._password_context,
            )

            if is_valid_password:
                return await self.create_tokens(user_id=user_dto.id)  # type: ignore[arg-type]

        raise InvalidCredentialsError()
