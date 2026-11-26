"""Обработчики кастомных ошибок для FastAPI."""

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from .base_response_error import BaseResponseError


def register_exception_handlers(app: FastAPI) -> None:
    """
    Регистрация обработчиков ошибок.

    :param app: Приложение FastAPI.
    :return: None.
    """

    @app.exception_handler(BaseResponseError)
    async def base_response_error_handler(request: Request, exc: BaseResponseError) -> JSONResponse:
        """
        Обработка ошибок ответов.

        :param request: Клиентский запрос.
        :param exc: Ошибка.
        :return: JSON-ответ с кодом и сообщением ошибки.
        """

        return JSONResponse(
            status_code=exc.code,
            content={'message': exc.message},
        )
