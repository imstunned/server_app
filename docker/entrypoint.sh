#!/bin/sh
# Точка входа контейнера: применяем миграции и запускаем приложение.
set -e

echo "Applying database migrations..."
alembic upgrade head

echo "Starting application..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
