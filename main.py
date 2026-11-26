"""Лабораторная работа №1. Первое приложение на FastAPI."""

from fastapi import FastAPI

app = FastAPI(
    title='Blog API',
    version='0.1.0',
    description='Учебный проект: серверное приложение блога на FastAPI.',
)


@app.get('/')
def hello_world() -> dict[str, str]:
    """Корневая точка доступа."""
    return {'message': 'Привет, мир!'}


@app.get('/about')
def about_page() -> dict[str, str]:
    """Информация о приложении."""
    return {'name': 'Мой блог', 'version': '1.0'}
