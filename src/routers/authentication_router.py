"""Роутер для аутентификации."""

from typing import Annotated
from typing import Any
from typing import Dict

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from src.controllers import AuthenticationController
from src.dependencies import get_authentication_controller
from src.schemas.requests import RefreshTokenRequest
from src.schemas.requests import VerifyAccessTokenRequest
from src.schemas.responses import DeleteExpiredTokensResponse
from src.schemas.responses import TokensResponse
from src.schemas.responses import VerifyAccessTokenResponse

authentication_router = APIRouter(
    prefix='/authentication',
    tags=['Аутентификация'],
    deprecated=False,
    dependencies=None,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            'description': 'Недействительный токен',
        },
        status.HTTP_401_UNAUTHORIZED: {
            'description': 'Недействительный access-токен',
        },
        status.HTTP_403_FORBIDDEN: {
            'description': 'Недействительный refresh-токен',
        },
    },
)


@authentication_router.post(
    path='/logout',
    summary='Выход из приложения',
    description='Удаляет refresh-токен (и связанные access-токены) из БД.',
    response_description='Пустой объект при успешном выходе.',
)
async def logout(
    refresh_token_request: RefreshTokenRequest,
    authentication_controller: Annotated[AuthenticationController, Depends(get_authentication_controller)],
) -> Dict[str, Any]:
    """
    Выход пользователя из приложения.
    """

    return await authentication_controller.logout_user(refresh_token_request=refresh_token_request)


@authentication_router.post(
    path='/verify_access_token',
    summary='Проверка access-токена',
    description='Проверяет подпись, срок действия и наличие токена в БД.',
    response_description='Текущий access-токен.',
)
async def verify_access_token(
    verify_access_token_request: VerifyAccessTokenRequest,
    authentication_controller: Annotated[AuthenticationController, Depends(get_authentication_controller)],
) -> VerifyAccessTokenResponse:
    """
    Проверка access-токена.
    """

    return await authentication_controller.verify_access_token(
        verify_access_token_request=verify_access_token_request,
    )


@authentication_router.post(
    path='/refresh_tokens',
    summary='Обновление пары токенов',
    description='Проверяет refresh-токен, удаляет его и выдаёт новую пару токенов.',
    response_description='Новая пара access/refresh токенов.',
)
async def refresh_tokens(
    refresh_token_request: RefreshTokenRequest,
    authentication_controller: Annotated[AuthenticationController, Depends(get_authentication_controller)],
) -> TokensResponse:
    """
    Обновление пары токенов.
    """

    return await authentication_controller.refresh_tokens(refresh_token_request=refresh_token_request)


@authentication_router.delete(
    path='/delete_expired_tokens',
    summary='Удаление просроченных токенов',
    description='Удаляет из БД все refresh-токены с истёкшим сроком действия.',
    response_description='Количество удалённых refresh-токенов.',
)
async def delete_expired_tokens(
    authentication_controller: Annotated[AuthenticationController, Depends(get_authentication_controller)],
) -> DeleteExpiredTokensResponse:
    """
    Удаление просроченных токенов.
    """

    return await authentication_controller.delete_expired_tokens()
