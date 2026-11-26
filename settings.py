"""Настройки приложения."""

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AppSettings(BaseSettings):
    """
    Настройки приложения.
    """

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    # База данных
    SQL_DSN: str = 'postgresql+asyncpg://postgres:qwerty@localhost:5432/blog_api'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'qwerty'
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_DB: str = 'blog_api'
    USERS_SQL_SCHEMA: str = 'users'
    POSTS_SQL_SCHEMA: str = 'post'

    # JWT
    SECRET_KEY: str = 'change-me-in-production'
    JWT_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRES_MINUTES: int = 60 * 24 * 30
    APPLICATION_ID: int = 1

    # Отладка
    IS_DEBUG: bool = False


app_settings = AppSettings()
