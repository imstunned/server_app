"""Лабораторная работа №4. Точка входа в приложение."""

from fastapi import FastAPI
from uvicorn import run

from src.exceptions import register_exception_handlers
from src.routers import authentication_router
from src.routers import authorization_router
from src.routers import post_router
from src.routers import user_router

app = FastAPI(
    title='Blog API',
    version='0.4.0',
    description='Учебный проект: серверное приложение блога на FastAPI + PostgreSQL + JWT.',
)

app.include_router(post_router)
app.include_router(user_router)
app.include_router(authorization_router)
app.include_router(authentication_router)

register_exception_handlers(app)


def main() -> None:
    """Запуск сервера."""
    run(
        app,
        host='127.0.0.1',
        port=8000,
    )


if __name__ == '__main__':
    main()
