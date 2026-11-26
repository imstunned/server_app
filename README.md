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
├── settings.py             # настройки приложения (pydantic-settings)
├── alembic/                # окружение и миграции Alembic
├── src/
│   ├── controllers/        # бизнес-логика конечных точек
│   ├── dependencies/       # зависимости FastAPI (DI)
│   ├── enums/              # перечисления (регулярки, сообщения)
│   ├── exceptions/         # кастомные ошибки и их обработчики
│   ├── interfaces/         # базовые интерфейсы контроллеров и репозиториев
│   ├── models/             # ORM-модели SQLAlchemy
│   ├── repositories/       # слой работы с данными (БД, внешние системы)
│   ├── routers/            # роутеры (группы конечных точек)
│   ├── schemas/            # Pydantic-схемы: common, DTO, requests, responses
│   └── utils/              # мапперы, работа с JWT и паролями
├── requirements/
│   └── requirements.txt    # зависимости проекта
├── docker/init-db.sql      # создание схем БД при старте контейнера
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
```

1. Скопируйте переменные окружения и при необходимости поправьте DSN:

   ```bash
   copy .env.example .env
   ```

2. Поднимите PostgreSQL (или используйте уже установленный):

   ```bash
   docker compose up -d database
   ```

   > Если порт `5432` уже занят локальной PostgreSQL, измените маппинг в
   > `docker-compose.yml` на `"5433:5432"` и укажите `:5433` в `SQL_DSN`.
   > Внутри docker-сети приложение всегда обращается к `database:5432`.

3. Примените миграции:

   ```bash
   alembic upgrade head
   ```

4. Запустите приложение:

   ```bash
   uvicorn main:app --reload
   ```

Документация API: <http://127.0.0.1:8000/docs>

Запуск всего стека в контейнерах:

```bash
docker compose up -d --build --wait
docker compose run --rm blog-api alembic upgrade head
```

## Схема БД

- схема `users`: таблицы `user` (пользователи), `refresh_token`, `access_token`;
- схема `post`: таблица `post` (посты, FK `author_id → users.user.id`).

Схемы создаются миграцией (а также скриптом `docker/init-db.sql` при первом
старте контейнера).

## Аутентификация (JWT)

| Метод | Путь | Назначение |
| --- | --- | --- |
| `POST` | `/user` | регистрация (пароль хэшируется bcrypt) |
| `POST` | `/authorization/login` | вход, выдаёт пару access/refresh токенов |
| `POST` | `/authentication/verify_access_token` | проверка access-токена |
| `POST` | `/authentication/refresh_tokens` | ротация пары токенов |
| `POST` | `/authentication/logout` | выход (удаление refresh-токена) |
| `DELETE` | `/authentication/delete_expired_tokens` | удаление просроченных токенов |

Пример:

```bash
curl -X POST http://127.0.0.1:8000/authorization/login \
  -H "Content-Type: application/json" \
  -d "{\"login\":\"login\",\"password\":\"qwerty123\"}"
```

```json
{"accessToken": "eyJhbGciOi...", "refreshToken": "eyJhbGciOi..."}
```

Секреты (`SECRET_KEY`, пароли БД) задаются в `.env`; в репозиторий файл не
попадает — используйте `.env.example` как шаблон.

Подробности по каждой лабораторной — в `CHANGELOG.md`.
