# CHANGELOG

Все ответы на вопросы из основной части лабораторных работ.

## Лабораторная работа №1 — основы FastAPI, Git, Docker

Вопросов в основной части нет.

Итог работы:

- создано первое приложение на FastAPI с эндпоинтами `GET /` и `GET /about`;
- заполнены `.gitignore` и `.dockerignore`;
- приложение контейнеризировано (`Dockerfile` + `docker-compose.yml`);
- зависимости зафиксированы в `requirements.txt` (способ «ручной», а не `pip freeze`).

## Лабораторная работа №2 — модели данных Pydantic и структура проекта

### Вопрос 1. За что отвечают параметры инициализации класса `ConfigDict`?

`BaseSchema.model_config = ConfigDict(...)`:

- `extra='ignore'` — при валидации лишние (не объявленные в схеме) поля входных данных
  не вызывают ошибку, а просто отбрасываются. Альтернативы: `'forbid'` (запретить),
  `'allow'` (сохранить в `model_extra`).
- `alias_generator=to_camel` — автоматически генерирует алиасы полей: в Python поля
  остаются в `snake_case` (`author_name`), а в JSON (Swagger, ответы API) — в `camelCase`
  (`authorName`). Это стандарт для REST API.
- `populate_by_name=True` — разрешает заполнять модель как по алиасу (`authorName`),
  так и по имени поля (`author_name`). Без этого работал бы только алиас.
- `from_attributes=True` — позволяет создавать схему из объекта с атрибутами
  (`model_validate(orm_object)`), то есть из моделей SQLAlchemy, а не только из словарей.

### Вопрос 2. За что отвечают параметры инициализации класса `Field`?

- `description` — описание поля, попадает в JSON-схему и в Swagger UI;
- `default` — значение по умолчанию (поле становится необязательным);
- `ge` / `gt` / `le` / `lt` — числовые ограничения (`ge=1` — значение ≥ 1);
- `min_length` / `max_length` — ограничения длины строки;
- `examples` — примеры значения для документации (`example` в Pydantic v2 устарел);
- `kw_only=True` — поле можно передать только по имени (защита от позиционных ошибок).

Примечание: в Pydantic v2 параметр `init_var` из методички не используется —
он относился к dataclass-моделям, а для `BaseModel` применяется `kw_only`.

### Вопрос 3. Зачем нужен класс `Path` из библиотеки FastAPI?

`Path` — это «параметризованная зависимость» для path-параметров. Она:

- объявляет, что параметр берётся из пути URL (а не из query/body);
- задаёт ограничения и валидацию (`ge=1` — ID должен быть положительным);
- добавляет описание и примеры в OpenAPI/Swagger;
- при нарушении ограничений автоматически возвращает `422 Unprocessable Entity`.

Без `Path` параметр тоже был бы path-параметром (по имени в шаблоне маршрута), но без
метаданных и валидации.

### Дополнительно

- Добавлены эндпоинты создания (`POST /post`), частичного обновления (`PATCH /post/{post_id}`)
  и удаления (`DELETE /post/{post_id}`) постов.
- В декораторах маршрутов указаны `summary`, `description`, `response_description`,
  `status_code`, `responses` и `tags`.
- Проект разбит на пакеты `controllers`, `dependencies`, `interfaces`, `repositories`,
  `routers`, `schemas`, `utils`.
- Docker-образ обновлён: зависимости теперь лежат в `requirements/requirements.txt`.

## Лабораторная работа №3 — базы данных, SQLAlchemy и миграции Alembic

### Вопрос 1. За что отвечают поля инициализации класса `SettingsConfigDict`?

- `env_file='.env'` — путь к файлу с переменными окружения, откуда читаются значения;
- `env_file_encoding='utf-8'` — кодировка этого файла (важно для кириллицы в Windows);
- `extra='ignore'` — переменные из `.env`, которых нет среди полей класса, не вызывают
  ошибку и просто игнорируются (в файле есть, например, `POSTGRES_HOST`, которого нет
  в настройках приложения).

Дополнительно можно указать `case_sensitive` (регистрозависимость имён переменных),
`env_prefix` (префикс, например `APP_`), `env_nested_delimiter` (для вложенных настроек).

### Вопрос 2. Объяснить значение параметров в функции `mapped_column`

- тип (`Integer`, `String(255)`, `Text`, `TIMESTAMP`, `Boolean`) — SQL-тип колонки;
- `primary_key=True` — колонка является первичным ключом;
- `autoincrement=True` — значение генерируется базой (`SERIAL`/`IDENTITY`);
- `index=True` — создать индекс по колонке (ускоряет поиск);
- `unique=True` — уникальность значений (например, `login`, `email`);
- `nullable=False` — запрет `NULL`;
- `default=...` — значение по умолчанию на стороне Python (ORM подставит при вставке);
- `server_default=...` — значение по умолчанию на стороне БД (`false`, `now()`, `NULL`);
- `comment='...'` — комментарий к колонке (попадает в схему БД и в миграцию);
- `ForeignKey(UserModel.id, ondelete='CASCADE')` — внешний ключ и поведение при удалении
  связанной записи.

### Вопрос 3. Зачем нужен параметр `echo` в `create_async_engine`?

`echo=True` включает логирование всех SQL-запросов (и параметров) в stdout через
`logging`. Это нужно для отладки: видно, какие запросы реально уходят в БД, как
формируются `INSERT/UPDATE/SELECT`, где появляются лишние запросы (проблема N+1).
В production `echo` выключают — иначе логи растут и в них попадают чувствительные
данные. В проекте значение берётся из настройки `IS_DEBUG`:
`create_async_engine(app_settings.SQL_DSN, echo=app_settings.IS_DEBUG)`.

### Что сделано

- добавлены настройки приложения (`settings.py`, `.env`, `.env.example`);
- созданы ORM-модели `UserModel`, `PostModel` и миксины `MixinAutoIdModel`,
  `MixinSoftDeleteModel` (базовая модель — `src/models/base.py`);
- настроен Alembic (асинхронный `env.py`, DSN из настроек, `include_schemas=True`)
  и сгенерирована миграция `init tables` (создаёт схемы `users` и `post`);
- реализован `BaseDbRepository` с методами `get_one_full_by_id`, `get_many_full`,
  `get_many_short`, `upsert`, `delete_one_by_id`;
- **дописан метод `upsert`**: если `id` не задан — создаётся объект, иначе
  загружается существующий и обновляются переданные поля;
- создан `UserController`, роутер `/user` и CRUD-эндпоинты пользователей;
- CRUD постов переведён с хранения в памяти на PostgreSQL;
- пароли пользователей хэшируются (passlib + bcrypt) при создании и обновлении;
- добавлены кастомные ошибки (`BaseCustomError`, `BaseResponseError`, `ConflictError`)
  и их обработчик (409 при дубликате логина);
- `docker-compose.yml` дополнен сервисом `database` (postgres:17) с healthcheck
  и томом для данных.

## Лабораторная работа №4 — аутентификация и авторизация с JWT

### Вопрос 1. Что произойдёт с access-токеном, если удалить refresh-токен в БД?

В модели `AccessTokenModel` есть внешний ключ
`refresh_id → users.refresh_token.id` с `ondelete='CASCADE'`. Поэтому при удалении
refresh-токена PostgreSQL каскадно удалит все связанные с ним access-токены.
Практические следствия:

- access-токен сразу становится недействительным, даже если его срок ещё не истёк
  (проверка `verify_access_token` ищет запись в БД и вернёт `401`);
- именно на этом построены `logout` и `refresh_tokens`: старый refresh-токен
  удаляется, вместе с ним умирает и старая пара токенов, после чего выдаётся новая.

### Вопрос 2. Зачем нужен `str` при определении родителей класса `RegexEnum`?

`class RegexEnum(str, Enum)` — это строковое перечисление. Наследование от `str`
даёт:

- значения являются обычными строками (`RegexEnum.JWT_TOKEN == '^[\\w-]+...'`),
  их можно передавать в `Field(pattern=...)`, `re`, `json.dumps` и т. п.;
- Pydantic и FastAPI сериализуют такое перечисление как строку в JSON и OpenAPI,
  без дополнительных конвертеров;
- без миксина `str` обычный `Enum` не был бы строкой: `f'{RegexEnum.JWT_TOKEN}'`
  дал бы `RegexEnum.JWT_TOKEN`, а JSON-сериализация потребовала бы `.value`.

### Вопрос 3. Почему контроллер для работы с токенами был вынесен в отдельный контроллер?

Потому что создание пары токенов — общая логика, которая нужна сразу нескольким
сценариям: вход (`AuthorizationController`), обновление пары
(`AuthenticationController`) и, потенциально, регистрация. Вынос в
`TokensController`:

- убирает дублирование (принцип DRY): `create_tokens` написан один раз;
- соблюдает единственную ответственность (SRP): выпуск токенов отдельно от
  проверки пароля и от проверки/отзыва токенов;
- упрощает тестирование и переиспользование — оба контроллера наследуются от
  `TokensController` и получают `create_tokens` бесплатно.

### Задание 1. Логика авторизации и аутентификации

1. **Регистрация** (`POST /user`): пароль хэшируется bcrypt (`CryptContext`), в БД
   хранится только хэш.
2. **Авторизация / вход** (`POST /authorization/login`): пользователь ищется по
   логину, пароль проверяется через `password_context.verify`. При успехе
   `TokensController.create_tokens` создаёт в БД refresh-токен, затем access-токен,
   связанный с refresh-токеном, и возвращает два JWT (claims: `user`, `jti`, `iat`,
   `exp`).
3. **Аутентификация запросов** (`POST /authentication/verify_access_token`):
   токен декодируется и проверяется подпись/срок (`python-jose`), затем
   `_check_token` сверяет `jti`, `user`, `iat`, `exp` с записью в БД. Если запись
   удалена (logout/refresh) — токен недействителен.
4. **Обновление пары** (`POST /authentication/refresh_tokens`): проверяется
   refresh-токен, старый удаляется (каскадом убивая старый access), выпускается
   новая пара — это ротация токенов.
5. **Выход** (`POST /authentication/logout`): refresh-токен удаляется из БД,
   каскадно удаляется access-токен.
6. **Очистка** (`DELETE /authentication/delete_expired_tokens`): удаляются
   refresh-токены с истёкшим `expire_at`.

### Задание 2. Зависимости репозиториев и контроллеров

Добавлены `get_access_token_repository`, `get_refresh_token_repository`,
`get_tokens_controller`, `get_authorization_controller`,
`get_authentication_controller` (по аналогии с лабораторной №3).

### Что сделано

- добавлены настройки JWT (`SECRET_KEY`, `JWT_ALGORITHM`,
  `ACCESS_TOKEN_EXPIRES_MINUTES`, `REFRESH_TOKEN_EXPIRES_MINUTES`);
- созданы модели `AccessTokenModel` и `RefreshTokenModel` и миграция
  `add token models`;
- созданы DTO токенов, схемы запросов (`LoginRequestSchema`, `RefreshTokenRequest`,
  `VerifyAccessTokenRequest`) и ответов (`TokensResponse`,
  `VerifyAccessTokenResponse`, `DeleteExpiredTokensResponse`);
- добавлены перечисления `RegexEnum` и `MessageEnum`, кастомные ошибки
  (`ExpiredJwtTokenError`, `InvalidAccessTokenError`, `InvalidCredentialsError`,
  `InvalidRefreshTokenError`, `InvalidTokenError`);
- реализованы утилиты `CommonUtils` (создание/декодирование JWT, хэширование и
  проверка пароля) и мапперы DTO;
- созданы репозитории токенов, контроллеры `TokensController`,
  `AuthenticationController`, `AuthorizationController`;
- добавлены роутеры `/authorization` и `/authentication` и подключены к приложению.
