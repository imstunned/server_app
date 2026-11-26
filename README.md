# Blog API — лабораторные работы по разработке серверных приложений

Учебный проект по методичке «Разработка серверных приложений»: REST API блога на
FastAPI с PostgreSQL, SQLAlchemy, Alembic и JWT-аутентификацией.

## Стек

- Python 3.12
- FastAPI + Uvicorn
- Pydantic v2 / pydantic-settings
- PostgreSQL 17, SQLAlchemy 2 (async), asyncpg
- Alembic (миграции)
- JWT (python-jose), passlib + bcrypt
- Docker / Docker Compose

## Ветки

| Ветка | Содержимое |
| --- | --- |
| `main` | точка старта: README, .gitignore, .dockerignore |
| `develop` | интеграционная ветка, сюда вливаются все лабораторные |
| `feature/lab1` | ЛР1 — основы FastAPI, Git, Docker |
| `feature/lab2` | ЛР2 — модели данных Pydantic и структура проекта |
| `feature/lab3` | ЛР3 — БД, SQLAlchemy, миграции Alembic |
| `feature/lab4` | ЛР4 — аутентификация и авторизация с JWT |

Каждая следующая ветка создаётся от `develop` после вливания предыдущей
лабораторной (merge request → `develop`).

## Структура проекта

```
.
├── main.py                 # точка входа, создание FastAPI-приложения
├── src/
│   ├── controllers/        # бизнес-логика конечных точек
│   ├── dependencies/       # зависимости FastAPI (DI)
│   ├── interfaces/         # базовые интерфейсы контроллеров и репозиториев
│   ├── repositories/       # слой работы с данными (БД, внешние системы)
│   ├── routers/            # роутеры (группы конечных точек)
│   ├── schemas/            # Pydantic-схемы и DTO
│   └── utils/              # мапперы, декораторы, итераторы
├── requirements/
│   └── requirements.txt    # зависимости проекта
├── Dockerfile
├── docker-compose.yml
├── CHANGELOG.md            # отчёт по лабораторным + ответы на вопросы
└── docs/                   # методичка в Markdown и изображения
```

## Материалы

- `docs/metodichka_servernye_prilozhenia.md` — методичка в Markdown
- `docs/images/` — изображения, извлечённые из методички
- `scripts/docx_dump.py` — скрипт конвертации `.docx` → Markdown + изображения

## Быстрый старт

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements/requirements.txt
uvicorn main:app --reload
```

Документация API: <http://127.0.0.1:8000/docs>

Запуск в контейнерах:

```bash
docker compose up -d --build --wait
```

Подробности по каждой лабораторной — в `CHANGELOG.md`.
