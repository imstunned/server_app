"""Общие зависимости приложения."""

from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from settings import app_settings
from .common_factories import get_sqlalchemy_async_session_generator

db_engine = create_async_engine(app_settings.SQL_DSN, echo=app_settings.IS_DEBUG)
async_session_factory = async_sessionmaker(bind=db_engine, expire_on_commit=False)
sqlalchemy_async_session_generator = get_sqlalchemy_async_session_generator(async_session_factory)

# Для зависимостей шифрования паролей
password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_context() -> CryptContext:
    """
    Зависимость для внедрения контекста шифрования паролей.

    :return: Контекст шифрования паролей.
    """

    return password_context
