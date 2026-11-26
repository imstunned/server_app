"""Лабораторная работа №3. Точка входа в приложение."""

from fastapi import FastAPI
from uvicorn import run

from src.exceptions import register_exception_handlers
from src.routers import post_router
from src.routers import user_router

app = FastAPI(
    title='Blog API',
    version='0.3.0',
    description='Учебный проект: серверное приложение блога на FastAPI + PostgreSQL.',
)

app.include_router(post_router)
app.include_router(user_router)

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
