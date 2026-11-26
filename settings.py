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

    # Отладка
    IS_DEBUG: bool = False


app_settings = AppSettings()
