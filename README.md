# Blog API — лабораторные работы по разработке серверных приложений

Учебный проект по методичке «Разработка серверных приложений»: REST API блога на
FastAPI с PostgreSQL, SQLAlchemy, Alembic и JWT-аутентификацией.

## Стек

- Python 3.12 в Docker-образе (локально проект проверен на 3.14)
- FastAPI + Uvicorn
- Pydantic v2 / pydantic-settings
- PostgreSQL 17, SQLAlchemy 2 (async), asyncpg
- Alembic (миграции)
- JWT (python-jose), passlib + bcrypt
- Docker / Docker Compose

## Ветки и теги

| Ветка | Содержимое |
| --- | --- |
| `main` | итоговая версия проекта (все лабораторные влиты) |
| `develop` | интеграционная ветка, сюда вливаются все лабораторные |
| `feature/lab1` | ЛР1 — основы FastAPI, Git, Docker |
| `feature/lab2` | ЛР2 — модели данных Pydantic и структура проекта |
| `feature/lab3` | ЛР3 — БД, SQLAlchemy, миграции Alembic |
| `feature/lab4` | ЛР4 — аутентификация и авторизация с JWT |

Схема работы (GitFlow): `feature/labN` → Merge Request → `develop` → `main`.
Каждая следующая ветка создаётся от `develop` после вливания предыдущей
лабораторной.

Теги: `lab1`, `lab2`, `lab3`, `lab4` — состояние на момент сдачи каждой работы,
`v1.0.0` — итоговая версия.

## Публикация на GitHub

Репозиторий уже инициализирован локально (ветки и коммиты готовы). Осталось
создать пустой репозиторий на GitHub (**без** README и .gitignore) и выполнить:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/push_to_github.ps1 `
    -RepoUrl https://github.com/ВАШ_ЛОГИН/server_app.git
```

или вручную:

```bash
git remote add origin https://github.com/ВАШ_ЛОГИН/server_app.git
git push -u origin main develop
git push -u origin feature/lab1 feature/lab2 feature/lab3 feature/lab4
```

После пуша в GitHub создайте Pull Request'ы `feature/labN → develop` и
`develop → main`.

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
├── docker/entrypoint.sh    # миграции + запуск uvicorn в контейнере
├── Dockerfile
├── docker-compose.yml
├── CHANGELOG.md            # отчёт по лабораторным + ответы на вопросы
├── docs/                   # методичка в Markdown и изображения
└── scripts/                # конвертация методички, публикация на GitHub
```

## Материалы

- `docs/metodichka_servernye_prilozhenia.md` — методичка в Markdown (все 7 ЛР)
- `docs/images/` — 12 изображений, извлечённых из методички
- `scripts/docx_dump.py` — конвертация `.docx` → Markdown + изображения
  (зависимости: `python-docx`, `pymupdf`, `pillow`)

```bash
python scripts/docx_dump.py metodichka_servernye_prilozhenia.docx
```

## Быстрый старт

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements/requirements.txt
```

> В репозитории уже есть готовое окружение `.venv` (Python 3.14) со всеми
> зависимостями проекта и библиотеками для чтения `.docx`/`.pdf`.

1. Скопируйте переменные окружения и при необходимости поправьте DSN:

   ```bash
   copy .env.example .env
   ```

2. Поднимите PostgreSQL (или используйте уже установленный):

   ```bash
   docker compose up -d database
   ```

   > Если порт `5432` уже занят локальной PostgreSQL, задайте другой порт на хосте:
   > `POSTGRES_PORT=5433 docker compose up -d database` (PowerShell:
   > `$env:POSTGRES_PORT='5433'`). Внутри docker-сети приложение всегда
   > обращается к `database:5432`.

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
```

Миграции применяются автоматически при старте контейнера
(`docker/entrypoint.sh` выполняет `alembic upgrade head` перед запуском Uvicorn).

## Схема БД

- схема `users`: таблицы `user` (пользователи), `refresh_token`, `access_token`;
- схема `post`: таблица `post` (посты, FK `author_id → users.user.id`).

Схемы создаются миграцией (а также скриптом `docker/init-db.sql` при первом
старте контейнера).

## Основные эндпоинты

| Метод | Путь | Назначение |
| --- | --- | --- |
| `GET` | `/post/many` | список постов |
| `GET` | `/post/{post_id}` | пост по ID |
| `POST` | `/post` | создание поста |
| `PATCH` | `/post/{post_id}` | обновление поста |
| `DELETE` | `/post/{post_id}` | удаление поста |
| `GET` | `/user/many` | список пользователей |
| `GET` | `/user/{user_id}` | пользователь по ID |
| `POST` | `/user` | создание пользователя |
| `PATCH` | `/user/{user_id}` | обновление пользователя |
| `DELETE` | `/user/{user_id}` | удаление пользователя |

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
