"""Роутер для авторизации."""

from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from src.controllers import AuthorizationController
from src.dependencies import get_authorization_controller
from src.schemas.requests import LoginRequestSchema
from src.schemas.responses import TokensResponse

authorization_router = APIRouter(
    prefix='/authorization',
    tags=['Авторизация'],
    deprecated=False,
    dependencies=None,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            'description': 'Недействительные учётные данные',
        },
    },
)


@authorization_router.post(
    path='/login',
    summary='Вход в приложение',
    description='Проверяет логин и пароль и возвращает пару JWT-токенов.',
    response_description='Пара access/refresh токенов.',
)
async def user_login(
    login_request: LoginRequestSchema,
    authorization_controller: Annotated[AuthorizationController, Depends(get_authorization_controller)],
) -> TokensResponse:
    """
    Вход пользователя в приложение.
    """

    return await authorization_controller.login_user(login_request=login_request)
