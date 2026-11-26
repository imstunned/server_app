"""Лабораторная работа №2. Точка входа в приложение."""

from fastapi import FastAPI
from uvicorn import run

from src.routers import post_router

app = FastAPI(
    title='Blog API',
    version='0.2.0',
    description='Учебный проект: серверное приложение блога на FastAPI.',
)

app.include_router(post_router)


def main() -> None:
    """Запуск сервера."""
    run(
        app,
        host='127.0.0.1',
        port=8000,
    )


if __name__ == '__main__':
    main()
