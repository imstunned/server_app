РАЗРАБОТКА СЕРВЕРНЫХ ПРИЛОЖЕНИЙ

Методическое пособие

Цели курса:

- Освоить современный стек технологий для создания серверных приложений на Python

- Научиться проектировать, разрабатывать и развёртывать REST API

- Получить практические навыки работы с инструментами серверной разработки

Используемые технологии:

- Язык программирования: Python

- Фреймворк: FastAPI

- Инструменты для работы с БД: PostgreSQL, SQLAlchemy, Alembic

- Дополнительные инструменты: Git, Docker, Pydantic, JWT

Полезные источники:

- Курс Python на stepik.org - "Поколение Python": курс для начинающих

- Продвинутый курс Python на stepik.org - "Поколение Python": курс для продвинутых

- Документация FastAPI -

- Официальная страница PostgreSQL -

- Документация SQLAlchemy -

- Документация Alembic -

- Официальная страница Docker -

- Документация Pydantic - https://docs.pydantic.dev/latest/

ЛАБОРАТОРНАЯ РАБОТА №1

ОСНОВЫ FASTAPI, GIT, DOCKER

Цель работы: Создать первое приложение на FastAPI, настроить систему контроля версий и контейнеризацию.

ВВЕДЕНИЕ

FastAPI - современный фреймворк для создания API на Python 3.6+. Основные преимущества:

- Высокая производительность (сравнима с Node.js и Go)

- Автоматическая документация (Swagger UI и ReDoc)

- Валидация данных на основе аннотаций типов

- Поддержка асинхронности

Пример самого простого приложения на FastAPI:

from fastapi import FastAPI

# Создаем приложение
app = FastAPI()

# Создаем эндпоинт (точку доступа)
@app.get("/")
def read_root():
 return {"message": "Hello World"}

Объяснение:

- from fastapi import FastAPI – импорт класса FastAPI из библиотеки fastapi

- FastAPI() - создает FastAPI приложение

- @app.get("/") - декоратор, для создания конечных точек. Первый параметр в скобках указывает адрес (URL) для конечной точки

- Функция возвращает данные в виде JSON с ответом {"message": "Hello World"}

В примере выше показана реализация конечной точки с HTTP-методом GET, который в большинстве случаев отвечает за получение данных от сервера. Рассмотрим примеры использования других основных HTTP-методов:

- POST: @app.post(‘/’) – создание данных на сервере

- PUT: @app.put(‘/’) – создание/обновление данных на сервере

- PATCH: @app.patch(‘/’) – частичное обновление данных на сервере

- DELETE: @app.delete(‘/’) – удаление данных на сервере

HTTP методы:

- GET – получить данные от сервера

- POST – создать новый ресурс или отправить данные для обработки

- PUT – обновить ресурс или создать новый, если его нет

- PATCH – частично обновить ресурс

- DELETE – удалить ресурс

- HEAD – аналогичен GET, но сервер возвращает только заголовки, без тела ответа

- OPTIONS – описать параметры соединения или поддерживаемые методы для ресурса

Идемпотентные методы: GET, PUT, DELETE, HEAD, OPTIONS

Безопасные методы: GET, HEAD OPTIONS

Идемпотентность: Означает, что многократное выполнение одного и того же запроса даст тот же результат, что и однократное (например, GET, PUT, DELETE). Повторный POST обычно создает дубликаты.

Безопасность: Означает, что метод не изменяет состояние сервера (например, GET, HEAD). Они используются только для чтения данных.

Основы GIT

Git – система для контроля версий, которая позволяет сохранять историю изменения кода, хранить репозиторий проекта на удалённом сервере, что позволяет дать доступ к проекту другим разработчикам, и, в крайнем случае, откатывать добавленные изменения в код.

Основные команды:

git init — Инициализация репозитория

git config — Настройки параметров конфигурации Git.

git status — Состояние рабочего каталога и индекса.

git add — Добавление изменений в индекс.

git reset — Отмена изменений в репозитории.

git commit — Сохранение изменений в локальном репозитории Git.

git log — Просмотр истории коммитов

git push — Отправка коммитов в удаленный репозиторий

git branch — Управление ветками

git switch — Переключение между ветками

git clone — Создание копии удаленного репозитория

git stash — Временное хранилище

git checkout — Работа с ветками, восстановление файлов и переключение на конкретные коммиты

git merge — Слияние изменений веток

git fetch — Загрузка обновлений из удаленного репозитория

git pull — Извлечение и слияние изменений

git diff — Просмотр различий между файлами

Основы Docker

Docker упаковывает ваше приложение в "контейнер", чтобы оно работало на любом компьютере.

Работа с образами

docker images или docker image ls - Показать список всех локальных образов.

docker pull <имя_образа>:<тег> - Скачать образ из репозитория (например, docker pull nginx:latest).

docker build -t <имя_образа> . - Собрать образ из Dockerfile в текущей директории.

docker rmi <id_образа> - Удалить указанный локальный образ.

docker push <имя_образа> - Загрузить образ в репозиторий.

Работа с контейнерами

docker ps - Показать запущенные контейнеры.

docker ps -a - Показать все контейнеры (включая остановленные).

docker run -d --name <имя_контейнера> <образ> - Запустить контейнер в фоновом режиме.

docker stop <имя_контейнера> - Остановить контейнер.

docker start <имя_контейнера> - Запустить остановленный контейнер.

docker rm <имя_контейнера> - Удалить остановленный контейнер.

docker exec -it <имя_контейнера> <команда> - Выполнить команду внутри running-контейнера (например, docker exec -it my-container bash).

docker logs <имя_контейнера> - Показать логи контейнера.

Docker Compose

docker-compose up -d - Запустить сервисы в фоне из docker-compose.yml.

docker-compose down - Остановить и удалить контейнеры, сети.

docker-compose ps - Показать статус сервисов проекта.

docker-compose logs <сервис> - Показать логи конкретного сервиса.

docker-compose build - Пересобрать образы для сервисов.

docker-compose exec <сервис> <команда> - Выполнить команду в running-контейнере сервиса.docker-compose up -d - Запустить сервисы в фоне из docker-compose.yml.

docker-compose down - Остановить и удалить контейнеры, сети.

docker-compose ps - Показать статус сервисов проекта.

docker-compose logs <сервис> - Показать логи конкретного сервиса.

docker-compose build - Пересобрать образы для сервисов.

docker-compose exec <сервис> <команда> - Выполнить команду в running-контейнере сервиса.

ОСНОВНАЯ ЧАСТЬ

1. Настройка Git

1. Заходим в профиль GitLab и создаём новый публичный проект

![img_001](images/img_001.png)

2. Возвращаемся в Pycharm и клонируем созданный репозиторий

3. Создаём новую ветку develop от ветки main и пушим её в удалённый репозиторий

4. Создаём новую ветку feature/lab1, в которой будем работать, от ветки develop

2. Создание файлов

1. Устанавливаем Python Interpreter с виртуальным окружением для клонированного репозитория

2. Устанавливаем зависимости с помощью команды: pip install “fastapi[standard]”

3. В корневой папке проекта создаём 5 файлов:

- main.py – основная точка входа в приложение

- requirements.txt – файл с зависимостями проекта

- Dockerfile – файл с docker сборкой проекта

- docker-compose.yml – файл для контейнеризации приложения

- .gitignore – файл с описанием файлов, которые будут игнорироваться гитом

- .dockerignore - файл с описанием файлов, которые будут игнорироваться докером

![img_002](images/img_002.png)

3. Создание FastAPI приложения в main.py

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
 return {"message": "Привет, мир!"}


@app.get("/about")
def about_page():
 return {"name": "Мой блог", "version": "1.0"}
```

Объяснение:

- app – корневое приложение FastAPI

- У нас есть 2 конечные точки с GET-методом: главная (/) и о блоге (/about)

- Каждая функция возвращает простой JSON

4. Запуск приложения

Открываем терминал и вводим:

fastapi dev main.py

После запуска команды должны будут высветиться следующие логи:

![img_003](images/img_003.png)

Для проверки корректности написания эндпоинтов необходимо будет перейти на адрес

На странице по указанному адресу должен находиться JSON {"message":"Привет, мир!"}

Теперь попробуем к URL в командной строке добавить /about:

На странице по указанному адресу должен находиться JSON {"name":"Мой блог","version":"1.0"}

Примечание: Для внесения изменений в код при возникающих багах, необходимо для начала остановить HTTP-сервер. Для этого зайдите в терминал с открытым сервером и нажмите Ctrl + C, после этого сервер должен будет остановиться.

5. Запись зависимостей проекта в requirements.txt

Существует 2 способа записи зависимостей проекта в отдельный файл в Python:

- 1 способ (Супер-супер-супер нежелательный)

Ввести в терминал команду

pip freeze > requirements.txt

```
annotated-types==0.7.0
anyio==4.11.0
certifi==2025.10.5
click==8.3.0
colorama==0.4.6
dnspython==2.8.0
email-validator==2.3.0
fastapi==0.119.0
fastapi-cli==0.0.13
fastapi-cloud-cli==0.3.1
h11==0.16.0
httpcore==1.0.9
httptools==0.7.1
httpx==0.28.1
idna==3.11
Jinja2==3.1.6
markdown-it-py==4.0.0
MarkupSafe==3.0.3
mdurl==0.1.2
pydantic==2.12.2
pydantic_core==2.41.4
Pygments==2.19.2
python-dotenv==1.1.1
python-multipart==0.0.20
PyYAML==6.0.3
rich==14.2.0
rich-toolkit==0.15.1
rignore==0.7.1
sentry-sdk==2.42.0
shellingham==1.5.4
sniffio==1.3.1
starlette==0.48.0
typer==0.19.2
typing-inspection==0.4.2
typing_extensions==4.15.0
urllib3==2.5.0
uvicorn==0.37.0
watchfiles==1.1.1
websockets==15.0.1
```

- 2 способ (правильный)

- Записывание зависимостей в файл вручную

```
fastapi==0.119.0
uvicorn==0.37.0
```

6. Файлы .gitignore и .dockerignore

Найти самостоятельно, как должны выглядит файлы .gitignore и .dockerignore

7. Контейнеризация приложения

Открываем файл Dockerfile и прописываем туда следующее:

```
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

FROM python:3.12-slim - берем готовый образ с Python 3.12

WORKDIR /app - создаем папку /app в контейнере

COPY requirements.txt . - копируем файл с зависимостями

RUN pip install -r requirements.txt - устанавливаем зависимости

COPY . . - копируем весь наш код

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] - команда для запуска приложения (uvicorn – раннер, main:app – точка входа в приложение и название корневого приложения FastAPI (у нас это main и app соответственно), --host, 0.0.0.0 – хост приложение, --port, 8000 – порт приложения)

Открываем файл docker-compose.yml и прописываем туда следующее:

```
services:
 blog-api:
 image: blog-api-image
 build:
 context: .
 dockerfile: Dockerfile
 container_name: blog-api
 ports:
 - "8000:8000"
 networks:
 - default

networks:
 default:
 driver: bridge
```

build: - собирает образ из Dockerfile в текущей директории
 context: .

dockerfile: Dockerfile

container_name: blog-api - задает имя контейнера как указано

ports:

- "8000:8000"- пробрасывает порт 8000 из контейнера на хост

networks:

- default - подключает контейнер к сети

default: - создает bridge-сеть для контейнеров

Для запуска приложения в контейнере необходимо будет ввести следующие команды:
docker compose build – сборка приложения

docker compose up -d --wait – запуск приложения из контейнера (-d – запуск в фоновом режиме, --wait – ожидает статуса running|healthy для сервисов внутри контейнера)

После запуска контейнера перейдите на адрес (или любой другой порт, который был указан при сборке контейнера). Если всё было правильно сделано, то вы увидите результат выполнения функции с декоратором для создания эндпоинта с корневым URL.

Остановка контейнера:

docker compose down

ЗАДАНИЯ

1. Создать ветку feature/lab1 от ветки develop

2. Повторить все шаги по написанию первого приложения

3. Проверить работоспособность приложения

4. Заполнить .gitignore и .dockerignore

5. Запушить ветку feature/lab1 на удалённый репозиторий и создать Merge Request в ветку develop

ЛАБОРАТОРНАЯ РАБОТА 2

МОДЕЛИ ДАННЫХ С PYDANTIC И СТРУКТУРА ПРОЕКТА

Цель работы: Научиться работать с Pydantic для валидации данных и организовать правильную структуру проекта.

ВВЕДЕНИЕ

Структура проекта

Пример структуры FastAPI проекта

my-blog/

├── routers/ # Эндпоинты API

│ ├── __init__.py

│ └── posts.py

├── schemas/ # Pydantic модели

│ ├── __init__.py

│ └── data_transfer_objects/

├── models/ # Модели данных

│ ├── __init__.py

│ └── post_model.py

├── utils/ # Вспомогательные функции

│ ├── __init__.py

│ └── mappers.py

├── dependencies/ # Зависимости FastAPI

│ ├── __init__.py

│ └── common.py

├── requirements.txt

├── Dockerfile

├── .gitignore

└── main.py

Что такое Pydantic модели и зачем их используют

Pydantic - это библиотека для валидации данных и управления настройками в Python.

Зачем нужны Pydantic модели:

- Валидация данных - автоматическая проверка, что данные соответствуют ожидаемым типам

- Сериализация - преобразование данных между Python-объектами и JSON

- Документация - автоматическое описание API в Swagger

- Безопасность - защита от неверных данных

Как построить Pydantic модель

```
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Базовая модель для создания поста
class PostCreate(BaseModel):
 title: str
 content: str
 author: str

# Модель для ответа (включает автоматически генерируемые поля)
class PostResponse(BaseModel):
 id: int
 title: str
 content: str
 author: str
 created_at: datetime
 updated_at: Optional[datetime] = None

 class Config:
 from_attributes = True # Позволяет создавать из ORM объектов
```

Объяснение:

- BaseModel - базовый класс для всех Pydantic моделей

- title: str - поле должно быть строкой

- Optional[datetime] - поле может быть datetime или None

- from_attributes = True - позволяет создавать модель из объектов БД

APIRouter - организация эндпоинтов

APIRouter позволяет разбивать API на модули вместо того, чтобы все писать в одном файле.

Зачем нужен APIRouter:

- Организация кода - разные сущности в разных файлах

- Переиспользование - можно использовать в нескольких приложениях

- Префиксы и теги - группировка эндпоинтов в документации

ОСНОВНАЯ ЧАСТЬ

1. Построение корректной структуры проекта

![img_004](images/img_004.png)

Проект должен включать в себя следующие пакеты:

- src/controllers – контроллеры для реализации основной логики конечных точек

- src/dependencies – зависимости FastAPI

- src/models – модели базы данных

- src/repositories – репозитории для разделения слоя взаимодействия с библиотеками для внешних систем (Запросы к БД, HTTP-соединения и тд)

- requirements – зависимости проекта

- src/routers – роутеры для объединения конечных точек с общим признаком

- src/schemas – Pydantic модели

- src/utils – утилиты (итераторы, декораторы, мапперы и тд)

Примечение: в пакет requirements/ необходимо перенести файл requirements.txt. После этого, необходимо будет поправить Dockerfile (самостоятельно)

2. Создание базовой Pydantic модели для будущих DTO (Data Transfer Object (Объекты переноса данных))

Открываем пакет schemas/common/ и создаём файл base_schema.py

![img_005](images/img_005.png)

В файл base_schema.py вставляем следующий код:

```
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
 """
 Базовая схема.
 """

 model_config = ConfigDict(
 extra='ignore',
 alias_generator=to_camel,
 populate_by_name=True,
 from_attributes=True,
 )
```

Вопрос 1: За что отвечают параметры инициализации класса ConfigDict?

Далее, в пакете schemas/common находим файл __init__.py и импортируем класс BaseSchema

```
from .base_schema import BaseSchema
```

3. Создание DTO

Для того, чтобы было удобнее перемещать данные от сервера к пользователю и наоборот, существуют DTO (Data Transfer Object). Они облегчают работу с данными: унифицируют одни и те же типы объектов в один класс и позволяют добавлять валидацию данных

Создадим первый полный DTO для постов:
В пакете src/schemas/data_transfer_objects создаём файл post_full_dto.py

Вставляем в него следующий код:

```
from typing import Optional

from pydantic import Field

from src.schemas.common import BaseSchema


class PostFullDto(BaseSchema):
 """
 Полный DTO постов.
 """

 id: Optional[int] = Field(
 description='ID поста',
 default=None,
 ge=1,
 init_var=True,
 kw_only=True,
 examples=[1]
 )
 author_name: str = Field(
 description='Имя автора поста',
 init_var=True,
 kw_only=True,
 examples=['Author']
 )
 content: str = Field(
 description='Текстовое содержание поста',
 init_var=True,
 kw_only=True,
 examples=['Post content']
 )
```

Вопрос 2: За что отвечают параметры инициализации класса Field?

4. Создание контроллера для работы с постами блога

Перед тем, как переходить к созданию конечных точек, необходимо определиться с тем, где будет лежать вся логика работы с постами. Для этого существуют контроллеры.

Создадим базовый интерфейс для контроллеров:

- Создаём пакет src/interfaces/

- В пакете src/interfaces/ создаём ещё один пакет controllers/

- В пакете src/interfaces/controllers создаём файл base_controller_interface.py

![img_006](images/img_006.png)

- Вставляем в этот файл следующий код

```
class BaseControllerInterface:
 """
 Базовый интерфейс контроллера.
 """
 pass
```

Создадим базовый интерфейс для репозиториев:

- В пакете src/interfaces создаём пакет repositories/

- В пакете src/interfaces/repositories создаём файл base_repository_interface.py

![img_007](images/img_007.png)

- Вставляем в этот файл следующий код

```
class BaseRepositoryInterface:
 """
 Базовый интерфейс репозитория.
 """
 pass
```

Каждый контроллер обычно использует репозиторий для взаимодействия с БД, HTTP-соединением и тд.

Для этого создадим репозиторий post_repository.py для работы с постами в пакете src/repositories/:

```
from typing import List
from typing import Optional

from src.interfaces.repositories import BaseRepositoryInterface
from src.schemas.data_transfer_objects import PostFullDto


class PostRepository(BaseRepositoryInterface):
 """
 Репозиторий для работы с постами.
 """

 def __init__(self, posts: List[PostFullDto]): # TODO: Заглушка, позже перейти на сессии БД
 self._posts = posts

 async def get_post_by_id(self, post_id: int) -> Optional[PostFullDto]:
 """
 Получение поста по его ID.

 :param post_id: ID поста.
 :return: Полный DTO поста.
 """
 for post in self._posts:
 if post.id == post_id:
 return post

 return None

 async def get_post_many(self) -> List[PostFullDto]:
 """
 Получение списка полных DTO постов.

 :return: Список полных DTO постов.
 """

 return self._posts
```

Теперь можем приступать к созданию класса PostController в пакете src/controllers

![img_008](images/img_008.png)

Вставляем в него следующий код:

```
from typing import List
from typing import Optional

from src.interfaces.controllers import BaseControllerInterface
from src.repositories import PostRepository
from src.schemas.data_transfer_objects import PostFullDto


class PostController(BaseControllerInterface):
 """
 Контроллер для работы с постами.
 """

 def __init__(self, post_repository: PostRepository):
 self._post_repository = post_repository

 async def get_post_by_id(self, post_id: int) -> Optional[PostFullDto]:
 """
 Получение поста по ID.

 :param post_id: ID поста.
 :return: Полный DTO поста.
 """

 return await self._post_repository.get_post_by_id(post_id=post_id)

 async def get_post_many(self) -> List[PostFullDto]:
 """
 Получение списка постов.

 :return: Список постов.
 """

 return await self._post_repository.get_post_many()
```

5. Создание FastAPI зависимостей

Что такое инъекция зависимостей («Dependency Injection»)

В программировании «Dependency Injection» означает, что у вашего кода есть способ объявить вещи, которые требуются для его работы и использования: «зависимости».

И затем эта система (в нашем случае FastAPI) позаботится о том, чтобы сделать всё необходимое для предоставления вашему коду этих зависимостей (сделать «инъекцию» зависимостей).

Это очень полезно, когда вам нужно:

- Обеспечить общую логику (один и тот же алгоритм снова и снова).

- Разделять соединения с базой данных.

- Обеспечить безопасность, аутентификацию, требования к ролям и т. п.

- И многое другое...

Всё это при минимизации повторения кода.

Для создания зависимостей существует отдельный пакет dependencies/

- Создадим в нём файл common_dependencies.py. В нём будет лежать функция для генерации списка постов (заглушка, в дальнейшем будет переход на работу с БД)

- from typing import List

from src.schemas.data_transfer_objects import PostFullDto

posts = [
 PostFullDto(id=1, author_name='Bob', content='52'),
 PostFullDto(id=2, author_name='Billy', content='67'),
 PostFullDto(id=3, author_name='John', content='Lorem ipsum')
]


async def get_posts() -> List[PostFullDto]:
 """
 Получение списка полных DTO постов.

 :return: Список полных DTO постов.
 """

 return posts

- В этом же пакете создадим repositories_dependencies.py. В нём будет зависимость для получения репозитория для работы с постами

```
from typing import Annotated
from typing import List

from fastapi import Depends

from src.repositories import PostRepository
from src.schemas.data_transfer_objects import PostFullDto
from .common_dependencies import get_posts


async def get_post_repository(posts: Annotated[List[PostFullDto], Depends(get_posts)]) -> PostRepository:
 """
 Зависимость для внедрения репозитория для работы с постами.

 :param posts: Список постов.
 :return: Репозиторий для работы с постами
 """

 return PostRepository(posts=posts)
```

- В этом же пакете создадим controllers_dependencies.py. В нём будет зависимость для получения контроллера для работы с постами

```
from typing import Annotated

from fastapi import Depends

from src.controllers import PostController
from src.repositories import PostRepository
from .repositories_dependencies import get_post_repository


async def get_post_controller(
 post_repository: Annotated[PostRepository, Depends(get_post_repository)]
) -> PostController:
 """
 Зависимость для внедрения контроллера для работы с постами.
 
 :param post_repository: Репозиторий для работы с постами.
 :return: Контроллер для работы с постами.
 """

 return PostController(post_repository=post_repository)
```

6. Роутер для работы с постами

Теперь, после создания всех необходимых репозиториев, контроллеров и зависимостей, можем приступить к написанию роутера и его внедрению в корневое FastAPI приложение

В пакете routers/ создаём файл post_router.py и вставляем в него следующий код:

```
from typing import Annotated
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path

from src.controllers import PostController
from src.dependencies import get_post_controller
from src.schemas.data_transfer_objects import PostFullDto

post_router = APIRouter(
 prefix='/post',
 tags=['Посты'],
 deprecated=False,
 dependencies=None
)


@post_router.get('/many')
async def get_post_many(post_controller: Annotated[PostController, Depends(get_post_controller)]) -> List[PostFullDto]:
 """
 Получение списка постов.
 """

 return await post_controller.get_post_many()


@post_router.get('/{post_id}')
async def get_post_by_id(
 post_controller: Annotated[PostController, Depends(get_post_controller)],
 post_id: int = Path(
 description='ID поста',
 ge=1,
 example=1
 )
) -> PostFullDto:
 """
 Получение информации о посте.
 """

 return await post_controller.get_post_by_id(post_id=post_id)
```

Вопрос 3: зачем нужен класс Path из библиотеки FastAPI?

Модифицируем файл main.py следующим образом:

```
from fastapi import FastAPI
from uvicorn import run

from src.routers import post_router

app = FastAPI()

app.include_router(post_router)


def main():
 """
 Запуск сервера.
 """

 run(
 app,
 host='127.0.0.1',
 port=8000
 )

if __name__ == '__main__':
 main()
```

Запустить сервер и протестировать получившийся результат

ЗАДАНИЯ

1. Создать новую ветку feature/lab2 от develop

2. Добавить конечные точки для создания, редактирования и удаления постов

3. Написать дополнительные параметры в декораторах для создания конечных точек

4. Обновить docker-образ приложения

5. Создать файл CHANGELOG.md и внести туда все ответы на вопросы в основной части

6. Запушить ветку feature/lab2 в удалённый репозиторий и создать Merge Request к ветке develop

ЛАБОРАТОРНАЯ РАБОТА 3

БАЗЫ ДАННЫХ, SQLALCHEMY И МИГРАЦИИ С ALEMBIC

Цель работы: Интегрировать PostgreSQL с SQLAlchemy ORM и настроить систему миграций.

ВВЕДЕНИЕ

Общий контекст и проблема

Прямое написание SQL-запросов в коде приложения, хотя и возможно, зачастую приводит к ряду сложностей:

- Небезопасность: Риск SQL-инъекций при неправильной обработке пользовательского ввода.

- Слабая типизация: Отсутствие проверки типов данных на уровне Python.

- "Версионность" БД: Трудности отслеживания изменений в структуре базы данных (схеме) при работе в команде и на разных стендах (разработка, тестирование, продакшен).

- Привязка к конкретной СУБД: Код, написанный под одну СУБД (например, SQLite), может не работать с другой (например, PostgreSQL).

Для решения этих проблем повсеместно используется технология ORM (Object-Relational Mapping) – прослойка, которая отображает таблицы базы данных в классы Python, а строки этих таблиц – в их экземпляры. Это позволяет разработчику работать с данными как с обычными объектами Python, что делает код более читаемым, безопасным и легко тестируемым.

SQLAlchemy

- Декларативные модели – это способ описать структуру таблиц БД в виде Python-классов. Этот подход интуитивно понятен, лаконичен и позволяет централизованно управлять метаданными всей базы данных.

- Сессии (Session) – это единый рабочий контекст, который управляет состоянием всех объектов, загруженных из базы данных или предназначенных для сохранения. Сессия отвечает за кеширование, отслеживание изменений и выполнение операций в рамках транзакции, обеспечивая целостность данных.

- CRUD-операции (Create, Read, Update, Delete) – это основа любого приложения, работающего с данными. Мы изучим, как выполнять эти операции не через сырые SQL-строки, а через методы ORM, что автоматически экранирует данные и предотвращает уязвимости.

PostgreSQL

- Подключение к БД – первый и обязательный шаг. Мы рассмотрим формирование корректной строки подключения (DSN), которая содержит все необходимые параметры: адрес сервера, порт, имя базы данных, логин и пароль.

- Настройка соединения критически важна для производительности и стабильности приложения. Сюда входит настройка пула соединений (который управляется SQLAlchemy), таймаутов, кодировки и других параметров, позволяющих эффективно управлять ресурсами.

Alembic

Alembic – это инструмент для миграций базы данных, тесно интегрированный с SQLAlchemy.

- Миграция – это скрипт, который описывает последовательность действий для применения изменений к схеме БД (например, добавление столбца, создание таблицы) или для их отката. Миграции являются аналогом систем контроля версий (как Git) для вашей базы данных.

- Создание и применение миграций – это процесс, позволяющий последовательно и контролируемо обновлять схему БД на разных окружениях, гарантируя их идентичность.

- Автогенерация миграций – мощная возможность Alembic, которая позволяет автоматически создавать скрипты миграций, сравнивая текущее состояние ваших декларативных моделей SQLAlchemy с предыдущей версией схемы БД. Это значительно ускоряет разработку и снижает количество человеческих ошибок.

ОСНОВНАЯ ЧАСТЬ

- Установка зависимостей для работы с SQLAlchemy и Alembic

В командной строке:

pip install sqlalchemy alembic asyncpg

- Создание файла с переменными окружения

В корневой папке проекта необходимо создать файл “.env”. Здесь будут храниться все секреты приложения, которые мы будем подтягивать из класса настроек Pydantic settings.

![img_009](images/img_009.png)

Открываем файл .env и записываем следующее:

# DB
SQL_DSN=postgresql+asyncpg://postgres:qwerty@localhost:5432/blog_api
POSTGRES_USER=postgres
POSTGRES_PASSWORD=qwerty
POSTGRES_HOST=localhost
POSTGRES_DB=blog_api
USERS_SQL_SCHEMA=users
POSTS_SQL_SCHEMA=post

SQL_DSN (SQL Data Source Name) – символическое назавание, которое предоставляет сведения о подключении в базе данных: postgresql – СУБД, asyncpg – драйвер для асинхронного подключения к БД, postgres – имя пользователя, qwerty – пароль, localhost – хост, 5432 – порт, blog_api – название БД

POSTGRES_USER – имя пользователя

POSTGRES_PASSWORD – пароль

POSTGRES_HOST – хост

POSTGRES_DB – название БД

USERS_SQL_SCHEMA – название схемы для сервиса пользователей

POSTS_SQL_SCHEMA – название схемы для сервиса постов

- Создание класса настроек для приложения

В терминале:

pip install pydantic_settings

В корневой папке проекта необходимо создать файл settings.py

![img_010](images/img_010.png)

Открыть файл и записать туда следующее:

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AppSettings(BaseSettings):
 """
 Настройки приложения.
 """

 model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

 SQL_DSN: str = 'postgresql+asyncpg://user:password@localhost:5432/db'
 USERS_SQL_SCHEMA: str = 'users'
 POSTS_SQL_SCHEMA: str = 'post'


app_settings = AppSettings()

Вопрос 1: Объяснить за что отвечают поля инициализации класса SettingsConfigDict

- Создание базовой декларативной модели БД

В пакете src/models создать файл base.py

Открыть файл и записать туда следующее:

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
 """
 Базовая модель для ORM.
 """
 __abstract__ = True

- Создание папки с настройками alembic

В корневой папке проекта создать папку с названием “alembic”

В терминале:

alembic init alembic

После выполнения в корневой папке проекта должен будет создаться файл alembic.ini и в папке <название проекта>/alembic должны будут появиться файлы: env.py, README, script.py.mako и папка versions

Открываем файл alembic.ini и комментируем строку с sqlalchemy.url (DSN мы будет напрямую импортировать из настроек)

# database URL. This is consumed by the user-maintained env.py script only.
# other means of configuring database URLs may be customized within the env.py
# file.
; sqlalchemy.url = driver://user:pass@localhost/dbname

Открываем файл alembic/env.py и записываем следующее:

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from settings import app_settings
from src.models import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option('sqlalchemy.url', app_settings.SQL_DSN)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
 fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
target_metadata = Base.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
 """Run migrations in 'offline' mode.

 This configures the context with just a URL
 and not an Engine, though an Engine is acceptable
 here as well. By skipping the Engine creation
 we don't even need a DBAPI to be available.

 Calls to context.execute() here emit the given string to the
 script output.

 """
 url = config.get_main_option("sqlalchemy.url")
 context.configure(
 url=url,
 target_metadata=target_metadata,
 literal_binds=True,
 dialect_opts={"paramstyle": "named"},
 render_as_batch=True,
 include_schemas=True
 )

 with context.begin_transaction():
 context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
 context.configure(
 connection=connection,
 target_metadata=target_metadata,
 render_as_batch=True,
 include_schemas=True
 )

 with context.begin_transaction():
 context.run_migrations()


async def run_async_migrations() -> None:
 """
 In this scenario we need to create an Engine
 and associate a connection with the context.
 """

 connectable = async_engine_from_config(
 config.get_section(config.config_ini_section, {}),
 prefix='sqlalchemy.',
 poolclass=pool.NullPool,
 )

 async with connectable.connect() as connection:
 await connection.run_sync(do_run_migrations)

 await connectable.dispose()


def run_migrations_online() -> None:
 """Run migrations in 'online' mode."""

 asyncio.run(run_async_migrations())


if context.is_offline_mode():
 run_migrations_offline()
else:
 run_migrations_online()

- Сборка образа PostgreSQL

Открываем файл docker-compose.yml и записываем новый сервис:

services:
 blog-api:
 image: blog-api-image
 build:
 context: .
 dockerfile: Dockerfile
 container_name: blog-api
 ports:
 - "8000:8000"
 networks:
 - default
 database:
 image: postgres:17
 container_name: database
 environment:
 - POSTGRES_USER=${POSTGRES_USER}
 - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
 - POSTGRES_HOST=${POSTGRES_HOST}
 - POSTGRES_DB=${POSTGRES_DB}
 ports:
 - 5432:5432
 networks:
 - default
 restart: always

В терминале:

docker compose build

docker compose up –d –wait

- Создание миксинов для моделей

Миксин – класс для добавления полей в основные модели

Создаём файлы mixin_auto_id_model.py и mixin_soft_delete_model.py в src/models

Записываем в них следующее

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class MixinAutoIdModel(Base):
 """
 Миксина для добавления автоинкрементного поля `id`.
 """

 __abstract__ = True

 id: Mapped[int] = mapped_column(
 Integer,
 primary_key=True,
 index=True,
 unique=True,
 autoincrement=True,
 comment='Идентификатор',
 sort_order=-100
 )

from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import expression

from .base import Base


class MixinSoftDeleteModel(Base):
 """
 Миксина для добавления полей метаданных удаления.
 """

 __abstract__ = True

 is_deleted: Mapped[bool] = mapped_column(
 Boolean,
 nullable=False,
 default=False,
 server_default=expression.false(),
 sort_order=100,
 comment='Удалено'
 )
 deleted_by: Mapped[Optional[int]] = mapped_column(
 Integer,
 nullable=True,
 default=None,
 server_default=expression.null(),
 comment='Удалил',
 sort_order=101
 )
 deleted_at: Mapped[Optional[datetime]] = mapped_column(
 TIMESTAMP(),
 nullable=True,
 default=None,
 server_default=expression.null(),
 comment='Время удаления',
 sort_order=102
 )

- Создание моделей для схемы пользователей

Создаём файл user_model.py

![img_011](images/img_011.png)

Открываем файл и записываем:

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings
from .mixin_auto_id_model import MixinAutoIdModel
from .mixin_soft_delete_model import MixinSoftDeleteModel


class UserModel(MixinAutoIdModel, MixinSoftDeleteModel):
 """
 Модель пользователя.
 """
 __abstract__ = False
 __tablename__ = 'user'
 __table_args__ = {
 'schema': app_settings.USERS_SQL_SCHEMA,
 }

 username: Mapped[str] = mapped_column(
 String(50),
 nullable=False,
 unique=True,
 comment='Никнейм пользователя',
 sort_order=-20
 )
 email: Mapped[str] = mapped_column(
 String(120),
 nullable=False,
 unique=True,
 comment='Почта',
 sort_order=-15
 )
 login: Mapped[str] = mapped_column(
 String(255),
 nullable=False,
 unique=True,
 comment='Логин',
 sort_order=-10
 )
 password: Mapped[str] = mapped_column(
 String(255),
 nullable=False,
 comment='Пароль',
 sort_order=-5
 )

- Создание моделей для постов

Создаём файл post_model.py

![img_012](images/img_012.png)

Открываем файл и записываем следующее:

from datetime import datetime

from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings
from .mixin_auto_id_model import MixinAutoIdModel
from .mixin_soft_delete_model import MixinSoftDeleteModel


class PostModel(MixinAutoIdModel, MixinSoftDeleteModel):
 """
 Модель постов.
 """
 __abstract__ = False
 __tablename__ = 'post'
 __table_args__ = {
 'schema': app_settings.POSTS_SQL_SCHEMA
 }

 name: Mapped[str] = mapped_column(
 String(255),
 nullable=False,
 comment='Название поста',
 sort_order=-50
 )
 content: Mapped[str] = mapped_column(
 Text,
 nullable=False,
 comment='Контент',
 sort_order=-40
 )
 created_at: Mapped[datetime] = mapped_column(
 TIMESTAMP(),
 nullable=False,
 default=text('NOW()'),
 comment='Создан',
 sort_order=-20
 )

Вопрос 2: Объяснить значение параметров в функции mapped_column

- Создание/обновление DTO для моделей

Теперь, когда у нас появились модели сущностей в базе данных, можно описать под них DTO:

Для пользователей

from pydantic import Field

from src.schemas.common import MixinIdSchema
from src.schemas.common import MixinSoftDeleteSchema


class UserFullDto(MixinIdSchema, MixinSoftDeleteSchema):
 """
 Полный DTO пользователя.
 """

 username: str = Field(
 description='Никнейм',
 init_var=True,
 kw_only=True,
 examples=['Username']
 )
 email: str = Field( # TODO: Добавить паттерн регулярки почты
 description='Почта',
 init_var=True,
 kw_only=True,
 examples=['example@mail.com']
 )
 login: str = Field(
 description='Логин',
 init_var=True,
 kw_only=True,
 examples=['login']
 )
 password: str = Field(
 description='Пароль',
 init_var=True,
 kw_only=True,
 examples=['qwerty']
 )

Для постов полный DTO сделать самостоятельно!!!

- Генерация миграции

В терминале:

alembic revision –aurogenerate –m “init tables”

После выполнения, в папке alembic/versions должна будет появиться новая миграция, внимательно посмотрите, верно ли сгенерировал Alembic миграцию (все ли поля добавлены, корректные ли значения по умолчанию и т.д.)

Если всё корректно, то:

- Создаём схемы в БД с теми названиями, которые были заложены в переменные окружения USERS_SQL_SCHEMA и POSTS_SQL_SCHEMA

- Проводим миграцию с помощью команды в терминале:

- alembic upgrade head

- или alembic upgrade <revision ID>

- Работа с сессиями

Так как у нас появилось уже 2 сущности, значит под каждую из них надо будет реализовывать свой отдельный репозиторий для взаимодействия с БД. Однако, для того чтобы не нарушать принцип DRY при написании методов для получения/создания/обновления/удаления объектов, создадим базовый репозиторий для взаимодействия с БД:

```
from typing import Generic
from typing import Optional
from typing import Type
from typing import TypeVar

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.interfaces.repositories import BaseRepositoryInterface
from src.models import MixinAutoIdModel
from src.schemas.common import BaseSchema

ModelType = TypeVar('ModelType', bound=MixinAutoIdModel)
FullSchema = TypeVar('FullSchema', bound=BaseSchema)
ShortSchema = TypeVar('ShortSchema', bound=BaseSchema)


class BaseDbRepository(BaseRepositoryInterface, Generic[ModelType, FullSchema, ShortSchema]):
 """
 Базовый репозиторий для работы с БД.
 """

 def __init__(
 self,
 async_db_session: AsyncSession,
 model_type: Type[ModelType],
 full_schema_type: Type[FullSchema],
 short_schema_type: Type[ShortSchema]
 ):
 self._async_db_session = async_db_session
 self._model_type = model_type
 self._full_schema_type = full_schema_type
 self._short_schema_type = short_schema_type

 @property
 def async_db_session(self) -> AsyncSession:
 """
 Получение асинхронной сессии в БД.

 :return: Асинхронная сессия.
 """

 return self._async_db_session

 @property
 def model_type(self) -> Type[ModelType]:
 """
 Получение класса основной модели ORM.

 :return: Класс модели ORM.
 """
 return self._model_type

 @property
 def short_schema_type(self) -> Type[ShortSchema]:
 """
 Получение краткого DTO.

 :return: Краткое DTO.
 """
 return self._short_schema_type

 @property
 def full_schema_type(self) -> Type[FullSchema]:
 """
 Получение полного DTO.

 :return: Полное DTO.
 """
 return self._full_schema_type

 async def commit(self) -> None:
 """
 Фиксация изменений в БД.

 :return: None.
 """

 await self._async_db_session.commit()

 async def get_one_full_by_id(self, object_id: int) -> Optional[FullSchema]:
 """
 Получение полного DTO по ID.

 :param object_id: ID объекта.
 :return: Полный DTO объекта.
 """
model = await self._async_db_session.get(self._model_type, object_id)
```

_id)
 if model:
 return self._full_schema_type.model_validate(obj=model)

 return None

 # TODO: Дописать метод
 async def upsert(self, dto: FullSchema) -> FullSchema:
 """
 Создание одного объекта в БД.

 :param dto: Полный DTO объекта.
 :return: Полный DTO объекта.
 """
 pass

 async def delete_one_by_id(self, object_id: int) -> bool:
 """
 Удаление одного объекта по ID.

 :param object_id: ID объекта.
 :return: None.
 """
 delete_statement = delete(
 self._model_type
 ).where(
 self._model_type.id == object_id
 )

 result = await self._async_db_session.execute(statement=delete_statement)

 return result.rowcount == 1

Обновляем старый репозиторий постов:

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import PostModel
from src.schemas.data_transfer_objects import PostFullDto
from .base_db_repository import BaseDbRepository


class PostRepository(BaseDbRepository[PostModel, PostFullDto, PostFullDto]):
 """
 Репозиторий для работы с постами.
 """

 def __init__(
 self,
 async_db_session: AsyncSession
 ):
 super().__init__(
 async_db_session=async_db_session,
 model_type=PostModel,
 full_schema_type=PostFullDto,
 short_schema_type=PostFullDto
 )

Создаём репозиторий для работы с пользователями

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import UserModel
from src.schemas.data_transfer_objects import UserFullDto
from .base_db_repository import BaseDbRepository


class UserRepository(BaseDbRepository[UserModel, UserFullDto, UserFullDto]):
 """
 Репозиторий для работы с пользователями.
 """

 def __init__(
 self,
 async_db_session: AsyncSession
 ):
 super().__init__(
 async_db_session=async_db_session,
 model_type=UserModel,
 full_schema_type=UserFullDto,
 short_schema_type=UserFullDto
 )

- Зависимости для прикручивания сессий к репозиториям

Создаём файл common_factories.py в пакете src/dependencies:

from typing import AsyncGenerator
from typing import Callable

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker


def get_sqlalchemy_async_session_generator(
 async_session_maker: async_sessionmaker[AsyncSession]
) -> Callable[[], AsyncGenerator[AsyncSession, None]]:
 async def sqlalchemy_async_session_generator() -> AsyncGenerator[AsyncSession, None]:
 """
 Генератор асинхронных сессий БД.

 :return: AsyncSession.
 """
 # TODO: Подумать над тем, чтобы перейти к контекстному менеджеру
 async_session = async_session_maker()
 try:
 yield async_session

 await async_session.commit()
 except SQLAlchemyError as exc:

 await async_session.rollback()
 await async_session.close()

 raise exc
 else:
 await async_session.close()

 return sqlalchemy_async_session_generator

В файле common_dependencies.py:

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from settings import app_settings
from .common_factories import get_sqlalchemy_async_session_generator

db_engine = create_async_engine(app_settings.SQL_DSN, echo=True)
async_session_factory = async_sessionmaker(bind=db_engine, expire_on_commit=False)
sqlalchemy_async_session_generator = get_sqlalchemy_async_session_generator(async_session_factory)

Вопрос 3: Зачем нужен параметр echo в create_async_engine?

Обновляем зависимости для репозиториев в repositories_dependencies.py:

from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories import PostRepository
from src.repositories import UserRepository
from .common_dependencies import sqlalchemy_async_session_generator


async def get_post_repository(
 async_db_session: Annotated[AsyncSession, Depends(sqlalchemy_async_session_generator)]
) -> PostRepository:
 """
 Зависимость для внедрения репозитория для работы с постами.

 :param async_db_session: Асинхронная сессия БД.
 :return: Репозиторий для работы с постами
 """

 return PostRepository(async_db_session=async_db_session)


async def get_user_repository(
 async_db_session: Annotated[AsyncSession, Depends(sqlalchemy_async_session_generator)]
) -> UserRepository:
 """
 Зависимость для внедрения репозитория для работы с пользователями.
 
 :param async_db_session: Асинхронная сессия БД.
 :return: Репозиторий для работы с пользователями.
 """

 return UserRepository(async_db_session=async_db_session)

ЗАДАНИЯ

- Создать ветку feature/lab3 от develop

- Дописать метод upsert в базовом репозитории для работы с БД

- Создать UserController – контроллер для работы с пользователями

- Создать отдельный роутер для работы с пользователями и прикрутить его к приложению

- Реализовать CRUD операции для пользователей и постов в виде конечных точек

- Запустить контейнер с серверным приложением и проверить корректность работы конечных точек

- Записать ответы на все вопросы в основной части в CHANGELOG.md

- Запушить ветку в удалённый репозиторий и создать Merge Request

ЛАБОРАТОРНАЯ РАБОТА 4

АУТЕНТИФИКАЦИЯ И АВТОРИЗАЦИЯ С JWT

Цель работы: Реализовать систему регистрации и входа с JWT-токенами.

ВВЕДЕНИЕ

1. JWT: Структура токенов, создание и верификация

JWT (JSON Web Token) - это открытый стандарт для создания токенов доступа, основанный на формате JSON. Используется для безопасной передачи информации между сторонами в виде компактного URL-безопасного строкового объекта.

Структура JWT

JWT состоит из трёх частей, разделенных точками:

header.payload.signature

1. Header (Заголовок)

Содержит метаданные о типе токена и алгоритме шифрования:

{

"alg": "HS256", // алгоритм подписи (HS256, RS256 и др.)

"typ": "JWT" // тип токена

}

После кодирования в Base64Url: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

2. Payload (Полезная нагрузка)

Содержит claims (утверждения) - данные о пользователе и дополнительную информацию:

Типы claims:

- Registered claims: стандартные поля (iss, exp, sub, aud и др.)

- Public claims: пользовательские поля

- Private claims: согласованные между сторонами данные

{

"sub": "1234567890", // subject (идентификатор пользователя)

"name": "John Doe",

"iat": 1516239022, // issued at (время создания)

"exp": 1516242622 // expiration time (время истечения)

}

После кодирования в Base64Url: eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ

3. Signature (Подпись)

Создается путем подписи кодированных header и payload с использованием секретного ключа:

signature = HMACSHA256(

base64UrlEncode(header) + "." + base64UrlEncode(payload),

secret_key

)

2. OAuth2: Password Flow в FastAPI

Что такое OAuth2 Password Flow?

Password Flow (поток паролей) позволяет клиенту отправлять имя пользователя и пароль напрямую для получения токена. Используется только для доверенных клиентов (например, собственное мобильное приложение).

Установка зависимостей:

pip install passlib bcrypt python-jose[cryptography]

Поток работы Password Flow:

- Запрос токена: Клиент отправляет username и password на /token

- Аутентификация: Сервер проверяет учетные данные

- Генерация токена: При успешной проверке создается JWT

- Использование токена: Клиент использует токен в заголовке Authorization: Bearer <token>

3. Хеширование паролей: Библиотека passlib с bcrypt

Хранение паролей в открытом виде опасно. При утечке базы данных злоумышленники получат доступ ко всем аккаунтам. Хеширование преобразует пароль в необратимую строку.

Почему bcrypt?

- Адаптивный алгоритм: Можно увеличивать сложность со временем

- Соль (salt): Автоматическое добавление случайных данных к паролю

- Защита от GPU-атак: Вычислительно сложен для параллельной обработки

Установка зависимостей:

pip install passlib[bcrypt]

Советы по безопасности:

- Минимальная длина пароля: 8 символов

- Используйте bcrypt с rounds=12 или выше

- Никогда не храните пароли в открытом виде

- Добавьте соль (salt) - bcrypt делает это автоматически

- Регулярно обновляйте алгоритмы хеширования

- Используйте проверку сложности паролей

- Реализуйте защиту от брутфорса (ограничение попыток входа)

ОСНОВНАЯ ЧАСТЬ

1. Установка зависимостей:

pip install passlib[bcrypt]

pip install passlib bcrypt python-jose[cryptography]

2. Создание моделей access_token и refresh_token

В пакете src/models создаём файл access_token_model.py и записываем следующий код:

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings
from .mixin_auto_id_model import MixinAutoIdModel
from .refresh_token_model import RefreshTokenModel
from .user_model import UserModel


class AccessTokenModel(MixinAutoIdModel):
 """
 Модель access-токена.
 """

 __abstract__ = False
 __tablename__ = 'access_token'
 __table_args__ = {
 'schema': app_settings.USERS_SQL_SCHEMA
 }

 user_id: Mapped[int] = mapped_column(
 Integer,
 ForeignKey(UserModel.id, ondelete='CASCADE'),
 nullable=False,
 comment='ID пользователя'
 )
 expire_at: Mapped[datetime] = mapped_column(
 DateTime(),
 nullable=False,
 comment='Срок действия access-токена'
 )
 created_at: Mapped[datetime] = mapped_column(
 DateTime(),
 server_default=func.now(),
 nullable=False,
 comment='Дата создания access-токена'
 )
 refresh_id: Mapped[int] = mapped_column(
 Integer,
 ForeignKey(RefreshTokenModel.id, ondelete='CASCADE'),
 nullable=False,
 comment='ID refresh-токена'
 )

Вопрос 1 – Что произойдёт с access-токеном, если удалить refresh-токен в БД?

В пакете src/models создаём файл refresh_token_model.py и записываем следующий код:

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from settings import app_settings
from .mixin_auto_id_model import MixinAutoIdModel
from .user_model import UserModel


class RefreshTokenModel(MixinAutoIdModel):
 """
 Модель refresh-токена
 """

 __abstract__ = False
 __tablename__ = 'refresh_token'
 __table_args__ = {
 'schema': app_settings.USERS_SQL_SCHEMA
 }

 user_id: Mapped[int] = mapped_column(
 Integer,
 ForeignKey(UserModel.id, ondelete='CASCADE'),
 nullable=False,
 comment='ID пользователя'
 )
 expire_at: Mapped[datetime] = mapped_column(
 DateTime(),
 nullable=False,
 comment='Дата истечения refresh-токена'
 )
 created_at: Mapped[datetime] = mapped_column(
 DateTime(),
 nullable=False,
 comment='Дата создания refresh-токена'
 )

3. Генерация миграций для создания таблиц токенов в БД

Создаём миграцию с помощью команды:

alembic revision –autogenerate –m “Add token models”

Зайдите в папку alembic/versions и проверьте построчно правильность генерации миграции (сверьте поля в моделях и в коде миграции)

Запускаем миграцию командой:

alembic upgrade head

4. Создание DTO для авторизации/аутентификации

Сперва нам нужно будет создать DTO для access_token_model и refresh_token_model (В дальнейших лабораторных вы должны будете самостоятельно определять DTO для новых моделей)

В пакете src/schemas/data_transfer_objects создаём файлы access_token_full_dto.py и refresh_token_full_dto.py

from datetime import datetime

from pydantic import Field

from src.schemas.common import MixinIdSchema


class AccessTokenFullDto(MixinIdSchema):
 """
 DTO access-токена.
 """

 user_id: int = Field(
 description='ID пользователя',
 ge=0,
 init_var=True,
 kw_only=True
 )
 expire_at: datetime = Field(
 description='Срок действия токена',
 init_var=True,
 kw_only=True
 )
 created_at: datetime = Field(
 description='Время создания токена',
 init_var=True,
 kw_only=True
 )
 refresh_id: int = Field(
 ge=1,
 description='ID refresh-токена',
 init_var=True,
 kw_only=True
 )

from datetime import datetime

from pydantic import Field

from src.schemas.common import MixinIdSchema


class RefreshTokenFullDto(MixinIdSchema):
 """
 DTO refresh-токена.
 """

 user_id: int = Field(
 description='ID пользователя',
 ge=0,
 init_var=True,
 kw_only=True
 )
 expire_at: datetime = Field(
 description='Срок действия токена',
 init_var=True,
 kw_only=True
 )
 created_at: datetime = Field(
 description='Время создания токена',
 init_var=True,
 kw_only=True
 )

Также нам понадобится ещё один DTO для аутентификации пользователя:

from datetime import datetime

from pydantic import Field

from src.schemas.common import MixinIdSchema


class TokenDto(MixinIdSchema):
 """
 DTO токена.
 """

 user_id: int = Field(
 ge=1,
 description='Идентификатор пользователя',
 init_var=True,
 kw_only=True
 )
 expire_at: datetime = Field(
 description='Срок действия токена',
 init_var=True,
 kw_only=True,
 examples=[datetime.now()]
 )
 created_at: datetime = Field(
 description='Дата и время создания токена',
 init_var=True,
 kw_only=True,
 examples=[datetime.now()]
 )

Он будет хранить в себе данные декодированного access-токена

Для валидации JWT-токенов создадим перечисление регулярных выражений. Создаём пакет enums в пакете src, в этом пакете создаём regex_enum.py:

from enum import Enum


class RegexEnum(str, Enum):
 """
 Перечисление регулярных выражений.
 """

 JWT_TOKEN = r'^[\w-]+\.[\w-]+\.[\w-]+$'

Вопрос 2 – зачем нужен str при определении родителей класса RegexEnum?

На будущее создаём схемы запросов и ответов для авторизации/аутентификации пользователя:

В пакете src/schemas/requests

from pydantic import Field

from src.schemas.common import BaseSchema


class LoginRequestSchema(BaseSchema):
 """
 Запрос для входа в систему.
 """

 login: str = Field(
 description='Почта пользователя',
 min_length=1,
 max_length=255,
 init_var=True,
 kw_only=True
 )
 password: str = Field(
 description='Пароль пользователя',
 min_length=1,
 max_length=255,
 init_var=True,
 kw_only=True
 )

from pydantic import Field

from src.enums import RegexEnum
from src.schemas.common import BaseSchema


class RefreshTokenRequest(BaseSchema):
 """
 Запрос для обновления токенов.
 """

 refresh_token: str = Field(
 pattern=RegexEnum.JWT_TOKEN.value,
 description='refresh-токен',
 init_var=True,
 kw_only=True,
 examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp']
 )

from pydantic import Field

from src.enums import RegexEnum
from src.schemas.common import BaseSchema


class VerifyAccessTokenRequest(BaseSchema):
 """
 Запрос для проверки токена.
 """

 access_token: str = Field(
 pattern=RegexEnum.JWT_TOKEN.value,
 description='access-токен',
 init_var=True,
 kw_only=True,
 examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp']
 )

В пакете src/schemas/responses

from pydantic import Field

from src.schemas.common import BaseSchema


class DeleteExpiredTokensResponse(BaseSchema):
 """
 Ответ на запрос удаления всех неактуальных refresh-токенов.
 """

 deleted_tokens_count: int = Field(
 description='Количество удаленных refresh-токенов',
 init_var=True,
 kw_only=True,
 examples=[1]
 )

from pydantic import Field

from src.enums import RegexEnum
from src.schemas.common import BaseSchema


class TokensResponse(BaseSchema):
 """
 Ответ на создание/обновление токенов.
 """

 access_token: str = Field(
 description='Токен доступа',
 pattern=RegexEnum.JWT_TOKEN.value,
 examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp']
 )
 refresh_token: str = Field(
 description='Токен обновления',
 pattern=RegexEnum.JWT_TOKEN.value,
 examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp']
 )

from pydantic import Field

from src.enums import RegexEnum
from src.schemas.common import BaseSchema


class VerifyAccessTokenResponse(BaseSchema):
 """
 Ответ на проверку access-токена.
 """

 access_token: str = Field(
 description='Токен доступа',
 pattern=RegexEnum.JWT_TOKEN.value,
 examples=['eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp']
 )

5. Создание репозиториев для работы с токенами

В пакете src/repositories

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import AccessTokenModel
from src.schemas.data_transfer_objects import AccessTokenFullDto
from .base_db_repository import BaseDbRepository


class AccessTokenRepository(BaseDbRepository[AccessTokenModel, AccessTokenFullDto, AccessTokenFullDto]):
 """
 Репозиторий для работы с access-токенами.
 """

 def __init__(
 self,
 async_db_session: AsyncSession
 ):
 super().__init__(
 async_db_session=async_db_session,
 model_type=AccessTokenModel,
 full_schema_type=AccessTokenFullDto,
 short_schema_type=AccessTokenFullDto
 )

from datetime import datetime

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import RefreshTokenModel
from src.schemas.data_transfer_objects import RefreshTokenFullDto
from src.schemas.responses import DeleteExpiredTokensResponse
from src.utils import DeleteExpiredTokensResponseMapper
from .base_db_repository import BaseDbRepository


class RefreshTokenRepository(BaseDbRepository[RefreshTokenModel, RefreshTokenFullDto, RefreshTokenFullDto]):
 """
 Репозиторий для работы с refresh-токенами.
 """

 def __init__(
 self,
 async_db_session: AsyncSession
 ):
 super().__init__(
 async_db_session=async_db_session,
 model_type=RefreshTokenModel,
 full_schema_type=RefreshTokenFullDto,
 short_schema_type=RefreshTokenFullDto
 )

 async def delete_expired_tokens(self) -> DeleteExpiredTokensResponse:
 """
 Удаление refresh-токенов, которые не актуальны.

 :return: Ответ с количеством удалённых refresh-токенов.
 """
 statement = delete(self.model_type).where(RefreshTokenModel.expire_at < datetime.now())
 result = await self._async_db_session.execute(statement=statement)

 return DeleteExpiredTokensResponseMapper.map_delete_expired_tokens_response(
 deleted_tokens_count=result.rowcount
 )

Метод delete_expired_tokens нам понадобится для удаления refresh-токенов в БД

6. Создание кастомных ошибок сервиса

Кастомные ошибки необходимы для:

1. Читаемость кода – понятные названия ошибок

2. Легкая обработка

3. Безопасность – кастомные ошибки не раскрывают внутренние детали ошибок сервера

4. Документация

Определим базовый класс ошибок. Для этого создаём новый пакет exceptions в пакете src, и создаём в нём файл base_custom_error.py:

class BaseCustomError(Exception):
 """
 Базовый класс ошибок.
 """

 def __init__(self, message: str):
 self._message = message

 @property
 def message(self) -> str:
 return self._message

После этого создаём перечисление для хранения сообщений об ошибках в одном месте (в одном классе). Создаём в пакете src/enums файл message_enum.py:

from enum import Enum


class MessageEnum(str, Enum):
 """
 Перечисление сообщений.
 """

 INVALID_ACCESS_TOKEN_ERROR_MESSAGE = 'Недействительный токен доступа'
 INVALID_REFRESH_TOKEN_ERROR_MESSAGE = 'Недействительный refresh-токен'
 INVALID_CREDENTIALS_ERROR_MESSAGE = 'Недействительные учётные данные'
 INVALID_TOKEN_ERROR_MESSAGE = 'Недействительный токен'
 EXPIRED_JWT_TOKEN_ERROR_MESSAGE = 'Срок действия jwt-токена истёк'

Возвращаемся обратно к ошибкам и создаём базовый класс ошибок ответов:

from .base_custom_erorr import BaseCustomError
from src.enums import MessageEnum


class BaseResponseError(BaseCustomError):
 """
 Базовый класс ошибок ответов.
 """

 def __init__(self, message: MessageEnum, code: int):
 super().__init__(message=message)
 self._code = code

 @property
 def code(self) -> int:
 return self._code

Теперь мы можем создать несколько кастомных ошибок, которые могут возникнуть при использовании сервиса пользователем:

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class ExpiredJwtTokenError(BaseResponseError):
 """
 Ошибка истечения срока действия access/refresh токена.
 """

 def __init__(self):
 super().__init__(message=MessageEnum.EXPIRED_JWT_TOKEN_ERROR_MESSAGE, code=HTTPStatus.BAD_REQUEST)

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class InvalidAccessTokenError(BaseResponseError):
 """
 Ошибка невалидного access-токена.
 """

 def __init__(self):
 super().__init__(message=MessageEnum.INVALID_ACCESS_TOKEN_ERROR_MESSAGE, code=HTTPStatus.UNAUTHORIZED)

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class InvalidCredentialsError(BaseResponseError):
 """
 Исключение, возникающее при неправильной аутентификации пользователя.
 """

 def __init__(self):
 super().__init__(message=MessageEnum.INVALID_CREDENTIALS_ERROR_MESSAGE, code=HTTPStatus.BAD_REQUEST)

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class InvalidRefreshTokenError(BaseResponseError):
 """
 Ошибка невалидного refresh-токена.
 """

 def __init__(self):
 super().__init__(message=MessageEnum.INVALID_REFRESH_TOKEN_ERROR_MESSAGE, code=HTTPStatus.FORBIDDEN)

from http import HTTPStatus

from src.enums import MessageEnum
from .base_response_error import BaseResponseError


class InvalidTokenError(BaseResponseError):
 """
 Ошибка невалидного JWT-токена.
 """

 def __init__(self):
 super().__init__(message=MessageEnum.INVALID_TOKEN_ERROR_MESSAGE, code=HTTPStatus.BAD_REQUEST)

7. Создание утилит для работы с DTO

У приложения могут быть разные утилиты: мапперы (сборка DTO), апдейтеры (обновление DTO), декораторы, итераторы и т.д.

Создаём пакет utils в src, добавляем в него файл common_utils.py

from typing import Union

from jose import jwt
from jose.exceptions import ExpiredSignatureError
from jose.exceptions import JWTError
from passlib.context import CryptContext

from settings import app_settings
from src.exceptions import ExpiredJwtTokenError
from src.exceptions import InvalidTokenError
from src.schemas.data_transfer_objects import AccessTokenFullDto
from src.schemas.data_transfer_objects import RefreshTokenFullDto
from src.schemas.data_transfer_objects import TokenDto
from .token_dto_mapper import TokenDtoMapper


class CommonUtils:
 """
 Базовые утилиты.
 """

 @staticmethod
 def create_jwt_token(token_dto: Union[AccessTokenFullDto, RefreshTokenFullDto]) -> str:
 """
 Создание JWT токена.

 :param token_dto: Сущность токена.
 :return: Токен.
 """

 token_dict = {
 'user': str(token_dto.user_id),
 'aud': str(token_dto.application_id),
 'exp': token_dto.expire_at.timestamp(),
 'iat': token_dto.created_at.timestamp(),
 'jti': str(token_dto.id),
 }
 return str(jwt.encode(token_dict, app_settings.SECRET_KEY, algorithm=app_settings.JWT_ALGORITHM))

 @staticmethod
 def decode_jwt_token(token: str) -> TokenDto:
 """
 Декодирование JWT токена.

 :param token: Токен.
 :return: Данные токена.
 :raise ExpiredJwtTokenError: Если срок действия токена истек.
 :raise InvalidTokenError: Если токен невалидный.
 """
 try:
 decoded_dict = jwt.decode(
 token=token,
 key=app_settings.SECRET_KEY,
 algorithms=[
 app_settings.JWT_ALGORITHM,
 ]
 )
 except ExpiredSignatureError:
 raise ExpiredJwtTokenError()
 except JWTError:
 raise InvalidTokenError()
 except Exception:
 raise
 return TokenDtoMapper.get_from_decoded_dict(decoded_dict=decoded_dict)

 @staticmethod
 def verify_password(plain_password: str, hashed_password: str, password_context: CryptContext) -> bool:
 """
 Проверка пароля.

 :param plain_password: Незашифрованный пароль.
 :param hashed_password: Зашифрованный пароль.
 :param password_context: Контекст хэширования.
 :return: Результат проверки пароля.
 """

 return bool(password_context.verify(plain_password, hashed_password))

Пока что здесь у нас будут храниться методы для работы с jwt-токенами

После создаём мапперы, которые понадобятся нам для сборки DTO’s:

from datetime import datetime
from datetime import timedelta

from settings import app_settings
from src.schemas.data_transfer_objects import AccessTokenFullDto
from src.schemas.data_transfer_objects import RefreshTokenFullDto


class AccessTokenDtoMapper:
 """
 Сборка DTO access-токенов.
 """

 @staticmethod
 def map_from_refresh_token(user_id: int, refresh_token_dto: RefreshTokenFullDto) -> AccessTokenFullDto:
 """
 Сборка access-токена, используя refresh-токен.

 :param user_id: ID пользователя.
 :param refresh_token_dto: DTO refresh-токена.
 :return: DTO access-токена.
 """

 return AccessTokenFullDto(
 user_id=user_id,
 expire_at=datetime.now() + timedelta(app_settings.ACCESS_TOKEN_EXPIRES_MINUTES),
 created_at=datetime.now(),
 refresh_id=refresh_token_dto.id
 )

from src.schemas.responses import DeleteExpiredTokensResponse


class DeleteExpiredTokensResponseMapper:
 """
 Маппер для ответа на запрос удаления всех неактуальных refresh-токенов.
 """

 @staticmethod
 def map_delete_expired_tokens_response(deleted_tokens_count: int) -> DeleteExpiredTokensResponse:
 """
 Сборка ответа на запрос удаления всех неактуальных refresh-токенов.

 :param deleted_tokens_count: Количество удалённых токенов.
 :return: Ответ на запрос удаления всех неактуальных refresh-токенов.
 """
 return DeleteExpiredTokensResponse(deleted_tokens_count=deleted_tokens_count)

from datetime import datetime
from datetime import timedelta

from settings import app_settings
from src.schemas.data_transfer_objects import RefreshTokenFullDto


class RefreshTokenDtoMapper:
 """
 Сборка DTO refresh-токенов.
 """

 @staticmethod
 def map_from_user_id(user_id: int) -> RefreshTokenFullDto:
 """
 Сборка DTO refresh-токена с помощью id пользователя.

 :param user_id: ID пользователя.
 :return: DTO refresh-токена.
 """

 return RefreshTokenFullDto(
 user_id=user_id,
 expire_at=datetime.now() + timedelta(app_settings.REFRESH_TOKEN_EXPIRES_MINUTES),
 created_at=datetime.now()
 )

from datetime import datetime
from typing import Any
from typing import Dict

from src.schemas.data_transfer_objects import TokenDto


class TokenDtoMapper:
 """
 Сборка сокращённой модели токена.
 """

 @staticmethod
 def get_from_decoded_dict(decoded_dict: Dict[str, Any]) -> TokenDto:
 """
 Маппинг сокращённой модели токена из словаря запроса.

 :param decoded_dict: Словарь из тела запроса.
 :return: Сокращённая модель токен.
 :raises HTTPException: Если необходимые для сборки ключи отсутствуют в словаре.
 """
 try:
 token_short_dto = TokenDto(
 id=int(decoded_dict['jti']),
 user_id=int(decoded_dict['user']),
 expire_at=datetime.fromtimestamp(decoded_dict['exp']),
 created_at=datetime.fromtimestamp(decoded_dict['iat'])
 )
 return token_short_dto
 except KeyError:
 raise

from src.schemas.responses import TokensResponse


class TokensResponseMapper:
 """
 Сборка схемы ответа на создание/обновление токенов.
 """

 @staticmethod
 def map_tokens_response(
 access_token: str,
 refresh_token: str
 ) -> TokensResponse:
 """
 Сборка схемы ответа на создание/обновление токенов.

 :param access_token: Токен доступа
 :param refresh_token: Токен обновления
 :return: Схема ответа на создание/обновление токенов
 """

 return TokensResponse(access_token=access_token, refresh_token=refresh_token)

from aiohttp import ClientResponse

from src.schemas.responses import VerifyAccessTokenResponse


class VerifyAccessTokenResponseMapper:
 """
 Сборка ответа на проверку access-токена.
 """

 @staticmethod
 def map_verify_access_token_response(access_token: str) -> VerifyAccessTokenResponse:
 """
 Сборка схемы ответа на проверку access-токена.

 :param access_token: access-токен.
 :return: Ответ на проверку access-токена.
 """

 return VerifyAccessTokenResponse(access_token=access_token)

 @staticmethod
 async def map_from_http_response(response: ClientResponse) -> VerifyAccessTokenResponse:
 """
 Сборка схемы ответа на создание/обновление токенов из HTTP-ответа.

 :param response: HTTP-ответ.
 :return: Схема ответа на создание/обновление токенов.
 """
 return VerifyAccessTokenResponse.model_validate(obj=await response.json())

!!! Утилиты зачастую создаются на этапе написания логики в контроллерах, когда появляется необходимость собрать, обновить объекты !!!

8. Контроллеры авторизации/аутентификации

Контроллер для работы с токенами

from src.interfaces.controllers import BaseControllerInterface
from src.repositories import AccessTokenRepository
from src.repositories import RefreshTokenRepository
from src.repositories import UserRepository
from src.schemas.responses import TokensResponse
from src.utils import AccessTokenDtoMapper
from src.utils import CommonUtils
from src.utils import RefreshTokenDtoMapper
from src.utils import TokensResponseMapper


class TokensController(BaseControllerInterface):
 """
 Контроллер для работы с токенами.
 """

 def __init__(
 self,
 user_repository: UserRepository,
 refresh_token_repository: RefreshTokenRepository,
 access_token_repository: AccessTokenRepository
 ):
 self._user_repository = user_repository
 self._refresh_token_repository = refresh_token_repository
 self._access_token_repository = access_token_repository

 async def create_tokens(self, user_id: int) -> TokensResponse:
 """
 Создание новой пары токенов.

 :return: Пара токенов.
 :raises ValueError: Если получено DTO пользователя с некорректным ID.
 """

 refresh_token_full_dto = RefreshTokenDtoMapper.map_from_user_id(user_id=user_id)
 refresh_token_full_dto = await self._refresh_token_repository.upsert(dto=refresh_token_full_dto)
 access_token_full_dto = AccessTokenDtoMapper.map_from_refresh_token(
 user_id=user_id,
 refresh_token_dto=refresh_token_full_dto
 )
 access_token_full_dto = await self._access_token_repository.upsert(dto=access_token_full_dto)
 await self._user_repository.update_last_login_at(user_id=user_id)

 return TokensResponseMapper.map_tokens_response(
 access_token=CommonUtils.create_jwt_token(token_dto=access_token_full_dto),
 refresh_token=CommonUtils.create_jwt_token(token_dto=refresh_token_full_dto)
 )

Контроллер аутентификации

from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from src.exceptions import ExpiredJwtTokenError
from src.exceptions import InvalidAccessTokenError
from src.exceptions import InvalidRefreshTokenError
from src.exceptions import InvalidTokenError
from src.repositories import AccessTokenRepository
from src.repositories import RefreshTokenRepository
from src.repositories import UserRepository
from src.schemas.data_transfer_objects import AccessTokenFullDto
from src.schemas.data_transfer_objects import RefreshTokenFullDto
from src.schemas.data_transfer_objects import TokenDto
from src.schemas.requests import RefreshTokenRequest
from src.schemas.requests import VerifyAccessTokenRequest
from src.schemas.responses import DeleteExpiredTokensResponse
from src.schemas.responses import TokensResponse
from src.schemas.responses import VerifyAccessTokenResponse
from src.utils import CommonUtils
from src.utils import VerifyAccessTokenResponseMapper
from .tokens_controller import TokensController


class AuthenticationController(TokensController):
 """
 Контроллер для аутентификации пользователя.
 """

 def __init__(
 self,
 user_repository: UserRepository,
 access_token_repository: AccessTokenRepository,
 refresh_token_repository: RefreshTokenRepository
 ):
 super().__init__(
 user_repository=user_repository,
 refresh_token_repository=refresh_token_repository,
 access_token_repository=access_token_repository
 )

 async def _check_token(self, token_dto: TokenDto, is_refresh: bool = False) -> bool:
 """
 Проверка корректности токена.

 :param token_dto: Краткая информация о токене.
 :param is_refresh: Флаг для определения типа токена.
 :return: Признак корректности токена.
 """
 token_dto_from_db: Optional[Union[AccessTokenFullDto, RefreshTokenFullDto]]
 if is_refresh:
 token_dto_from_db = await self._refresh_token_repository.get_one_full_by_id(
 object_id=token_dto.id # type: ignore[arg-type]
 )
 else:
 token_dto_from_db = await self._access_token_repository.get_one_full_by_id(
 object_id=token_dto.id # type: ignore[arg-type]
 )
 if token_dto_from_db:
 is_valid_token = (
 token_dto_from_db.user_id == token_dto.user_id and
 token_dto_from_db.created_at == token_dto.created_at and
 token_dto_from_db.expire_at == token_dto.expire_at
 )
 if is_valid_token:
 return True

 return False

 return False

 async def logout_user(self, refresh_token_request: RefreshTokenRequest) -> Dict[str, Any]:
 """
 Выход пользователя из приложения.

 :param refresh_token_request: Данные для проверки refresh токена.
 :return: При успешной проверке возвращается новая пара токенов.
 """
 token_dto = CommonUtils.decode_jwt_token(token=refresh_token_request.refresh_token)
 if await self._check_token(token_dto=token_dto, is_refresh=True):
 await self._refresh_token_repository.delete_one_by_id(
 object_id=token_dto.id # type: ignore[arg-type]
 )

 return dict()

 raise InvalidRefreshTokenError()

 async def verify_access_token(
 self,
 verify_access_token_request: VerifyAccessTokenRequest
 ) -> VerifyAccessTokenResponse:
 """
 Проверка access токена.

 :param verify_access_token_request: Данные для проверки access токена.
 :return: При успешной проверке возвращается текущий access токен и успешный ответ.
 :raise InvalidAccessTokenError: Если access токен невалиден.
 """
 token_dto: Optional[TokenDto] = None
 try:
 token_dto = CommonUtils.decode_jwt_token(token=verify_access_token_request.access_token)
 except (ExpiredJwtTokenError, InvalidTokenError) as exc:
 print(f'Error decode access token: {exc}')

 if token_dto:
 if await self._check_token(token_dto=token_dto):
 user_dto = await self._user_repository.get_one_full_by_id(object_id=token_dto.user_id)
 if user_dto:
 if not user_dto.is_deleted:
 return VerifyAccessTokenResponseMapper.map_verify_access_token_response(
 access_token=verify_access_token_request.access_token
 )

 raise InvalidAccessTokenError()

 async def refresh_tokens(self, refresh_token_request: RefreshTokenRequest) -> TokensResponse:
 """
 Проверка refresh токена и создание новой пары токенов.

 :param refresh_token_request: Данные для проверки refresh токена.
 :return: При успешной проверке возвращается текущий refresh токен и успешный ответ.
 """
 token_dto: Optional[TokenDto] = None
 try:
 token_dto = CommonUtils.decode_jwt_token(token=refresh_token_request.refresh_token)
 except (ExpiredJwtTokenError, InvalidTokenError) as exc:
 print(f'Error decode refresh token: {exc}')

 if token_dto:
 if await self._check_token(token_dto=token_dto, is_refresh=True):
 user_dto = await self._user_repository.get_one_full_by_id(object_id=token_dto.user_id)
 if user_dto:
 if not user_dto.is_deleted:
 await self._refresh_token_repository.delete_one_by_id(object_id=token_dto.id)

 return await self.create_tokens(user_id=user_dto.id)

 raise InvalidRefreshTokenError()

 async def delete_expired_tokens(self) -> DeleteExpiredTokensResponse:
 """
 Удаление просроченных токенов.

 :return: Ответ с количеством удалённых refresh-токенов.
 """

 return await self._refresh_token_repository.delete_expired_tokens()

Контроллер авторизации:

from passlib.context import CryptContext

from src.exceptions import InvalidCredentialsError
from src.repositories import AccessTokenRepository
from src.repositories import RefreshTokenRepository
from src.repositories import UserRepository
from src.schemas.requests import LoginRequestSchema
from src.schemas.responses import TokensResponse
from src.utils import CommonUtils
from .tokens_controller import TokensController


class AuthorizationController(TokensController):
 """
 Контроллер для авторизации пользователя.
 """

 def __init__(
 self,
 user_repository: UserRepository,
 access_token_repository: AccessTokenRepository,
 refresh_token_repository: RefreshTokenRepository,
 password_context: CryptContext
 ):
 super().__init__(
 user_repository=user_repository,
 refresh_token_repository=refresh_token_repository,
 access_token_repository=access_token_repository
 )
 self._password_context = password_context

 async def login_user(self, login_request: LoginRequestSchema) -> TokensResponse:
 """
 Вход пользователя в приложение

 :param login_request: Данные для входа пользователя
 :return: При успешном входе возвращается пара токенов и информация о сессии
 """
 user_dto = await self._user_repository.get_user_by_login(login_request.login)

 if user_dto:
 is_valid_password = CommonUtils.verify_password(
 plain_password=login_request.password,
 hashed_password=user_dto.password,
 password_context=self._password_context
 )

 if is_valid_password:
 return await self.create_tokens(user_id=user_dto.id)

 raise InvalidCredentialsError()

Вопрос 3 – Почему контроллер для работы с токенами был вынесен как отдельный контроллер?

Задание 1 – Разобраться в логике авторизации и аутентификации самостоятельно

8. Зависимости репозиториев и контроллеров

В файл common_dependencies.py добавляем зависимость шифрования паролей:

from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from settings import app_settings
from .common_factories import get_sqlalchemy_async_session_generator

db_engine = create_async_engine(app_settings.SQL_DSN, echo=True)
async_session_factory = async_sessionmaker(bind=db_engine, expire_on_commit=False)
sqlalchemy_async_session_generator = get_sqlalchemy_async_session_generator(async_session_factory)

# Для зависимостей шифрования паролей
password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

Задание 2 – Самостоятельно создать зависимости репозиториев и контроллеров по аналогии с тем, что делали в прошлых лабораторных

9. Определение конечных точек

Создаём 2 отдельных роутера:

Для авторизации

from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from src.controllers import AuthorizationController
from src.dependencies import get_authorization_controller
from src.schemas.requests import LoginRequestSchema
from src.schemas.responses import TokensResponse

authorization_router = APIRouter(
 prefix='/authorization',
 tags=['Авторизация'],
 deprecated=False,
 dependencies=None
)


@authorization_router.post(path='/login')
async def user_login(
 login_request: LoginRequestSchema,
 authorization_controller: Annotated[AuthorizationController, Depends(get_authorization_controller)]
) -> TokensResponse:
 """
 Вход пользователя в приложение.
 """
 return await authorization_controller.login_user(login_request=login_request)

Для аутентификации:

from typing import Annotated
from typing import Any
from typing import Dict

from fastapi import APIRouter
from fastapi import Depends

from src.controllers import AuthenticationController
from src.dependencies import get_authentication_controller
from src.schemas.requests import RefreshTokenRequest
from src.schemas.requests import VerifyAccessTokenRequest
from src.schemas.responses import TokensResponse
from src.schemas.responses import VerifyAccessTokenResponse

authentication_router = APIRouter(
 prefix='/authentication',
 tags=['Авторизация'],
 deprecated=False,
 dependencies=None
)


@authentication_router.post(path='/logout')
async def logout(
 refresh_token_request: RefreshTokenRequest,
 authentication_controller: Annotated[AuthenticationController, Depends(get_authentication_controller)]
) -> Dict[str, Any]:
 """
 Выход пользователя из приложения
 """
 return await authentication_controller.logout_user(refresh_token_request=refresh_token_request)


@authentication_router.post(path='/verify_access_token')
async def verify_access_token(
 verify_access_token_request: VerifyAccessTokenRequest,
 authentication_controller: AuthenticationController = Depends(get_authentication_controller)
) -> VerifyAccessTokenResponse:
 """
 Проверка access-токена.
 """
 return await authentication_controller.verify_access_token(verify_access_token_request=verify_access_token_request)


@authentication_router.post(path='/refresh_tokens')
async def refresh_tokens(
 refresh_token_request: RefreshTokenRequest,
 authentication_controller: AuthenticationController = Depends(get_authentication_controller)
) -> TokensResponse:
 """
 Обновление пары токенов.
 """
 return await authentication_controller.refresh_tokens(refresh_token_request=refresh_token_request)

10. Включение роутеров в основное приложение

from fastapi import FastAPI
from uvicorn import run

from src.routers import authentication_router
from src.routers import authorization_router
from src.routers import post_router

app = FastAPI()

app.include_router(post_router)
app.include_router(authorization_router)
app.include_router(authentication_router)


def main():
 """
 Запуск сервера.
 """

 run(
 app,
 host='127.0.0.1',
 port=8000
 )


if __name__ == '__main__':
 main()

ЗАДАНИЯ

- Создать ветку feature/lab4 от develop

- Создать таблицы access_token и refresh_token в БД

- Создать контроллеры авторизации и аутентификации пользователей

- Создать конечные точки для авторизации пользователя, проверки access_token, обновления пары токенов и выхода пользователя из приложения

- Запустить контейнер с серверным приложением и проверить корректность работы конечных точек

- Записать ответы на все вопросы в основной части в CHANGELOG.md

- Запушить ветку в удалённый репозиторий и создать Merge Request

ЛАБОРАТОРНАЯ РАБОТА 5

МОНТИРУЕМЫЕ ПРИЛОЖЕНИЯ, MIDDLEWARE И АДМИН-ПАНЕЛЬ

Цель работы: Добавить монтируемые приложения в проект, реализовать промежуточное ПО сессии и создать админ-панель для пользователей

ВВЕДЕНИЕ:

Монтируемые приложения в FastAPI

Монтируемые приложения — это механизм, позволяющий встроить одно независимое веб-приложение внутрь другого по определённому пути. Представьте, что у вас есть главный сайт, и вы хотите добавить к нему блог или админ-панель как отдельный раздел. Монтирование позволяет сделать это чисто и организованно.

Когда вы монтируете приложение, все запросы, начинающиеся с указанного пути, автоматически передаются на обработку в это вложенное приложение. Например, если вы монтируете приложение по пути "/admin", то запрос "/admin/dashboard" будет обработан монтируемым приложением, а не основным.

Ключевые особенности:

- Полная изоляция: Монтируемое приложение работает независимо от основного. Оно имеет собственные маршруты, зависимости и обработчики ошибок.

- Разделение ответственности: Можно разделить большую систему на логические модули. Например, основное API, документацию, статические файлы и админ-панель могут быть разными монтируемыми приложениями.

- Переиспользование: Можно создать универсальное приложение (например, для аутентификации или мониторинга) и монтировать его в разные проекты.

- Разные настройки: Каждое монтируемое приложение может иметь свою конфигурацию, свои middleware и свои зависимости.

Типичные сценарии использования:

- Подключение инструментов мониторинга или документации

- Создание отдельных API версий

- Разделение публичной и административной частей приложения

Middleware в FastAPI

Middleware — это посредники между входящим запросом и вашим приложением, а также между ответом приложения и пользователем. Они обрабатывают запросы и ответы на глобальном уровне, до того как запрос попадёт в конкретный маршрут и после того как маршрут сформирует ответ.

Принцип работы:

Middleware работают цепочкой. Запрос проходит через все middleware последовательно, затем обрабатывается вашим маршрутом, и затем ответ проходит через те же middleware в обратном порядке.

Для чего используются middleware?

- Логирование: Запись информации о каждом запросе — кто, когда, что запросил, сколько времени заняла обработка.

- Аутентификация и авторизация: Проверка прав доступа пользователей перед обработкой запроса.

- Обработка CORS: Настройка правил для кросс-доменных запросов, чтобы ваш API могли использовать фронтенд-приложения с других доменов.

- Сжатие ответов: Автоматическое сжатие данных перед отправкой клиенту для экономии трафика.

- Ограничение запросов (Rate Limiting): Защита от злоупотреблений путём ограничения количества запросов от одного клиента.

- Обработка ошибок: Глобальный перехват и унифицированная обработка исключений.

- Добавление заголовков: Автоматическое добавление технических заголовков к каждому ответу.

- Валидация запросов: Предварительная проверка корректности входящих данных.

Типы middleware в FastAPI:

- Встроенные middleware: FastAPI предоставляет готовые middleware для задач, таких как обработка CORS или сжатие ответов.

- Стандартные middleware: Можно использовать совместимые middleware, созданные для работы с совместимыми фреймворками.

- Пользовательские middleware: Вы можете создавать собственные middleware для реализации специфической бизнес-логики.

Админ-панель

Админ-панель (панель администратора) — это специальный интерфейс для управления содержимым, данными и настройками веб-приложения. Это закрытый раздел сайта, доступный только авторизованным пользователям с соответствующими правами.

Ключевые компоненты админ-панели:

- Аутентификация и авторизация: Механизмы входа и разграничения прав доступа.

- Управление данными: CRUD-интерфейс (создание, чтение, обновление, удаление) для сущностей приложения.

- Мониторинг и аналитика: Графики, статистика, логи активности пользователей.

- Управление пользователями: Регистрация, блокировка, назначение ролей.

- Конфигурация системы: Настройки приложения, управление кэшем, очереди задач.

Зачем нужна админ-панель?

1. Эффективное управление контентом

- Позволяет не-техническим специалистам обновлять содержимое сайта

- Упрощает добавление новых товаров, статей, пользователей

- Избавляет от необходимости писать SQL-запросы или использовать командную строку

2. Безопасность

- Централизованное управление правами доступа

- Аудит действий администраторов

- Защита от прямого доступа к базе данных

3. Экономия времени разработки

- Готовая реализация стандартных операций

- Единый интерфейс для всех сущностей

- Автоматическая генерация форм на основе моделей данных

4. Мониторинг и аналитика

- Просмотр ключевых метрик приложения в реальном времени

- Анализ поведения пользователей

- Отслеживание ошибок и проблем

5. Техническое обслуживание

- Управление настройками приложения

- Просмотр логов

- Очистка кэша, переиндексация поиска

Типы админ-панелей:

- Автоматически сгенерированные: Создаются на основе моделей данных. Быстро настраиваются, но могут быть ограничены в кастомизации.

- Кастомные (настраиваемые): Разрабатываются под конкретные требования проекта. Требуют больше времени, но полностью соответствуют нуждам бизнеса.

- Гибридные: Берут за основу сгенерированную панель и дорабатывают под конкретные нужды.

ОСНОВНАЯ ЧАСТЬ

1. Добавление объекта сессии клиента

Создаём новый пакет builtin_types/ в пакете src/, добавляем в него файлы session.py и session_middleware.py

В файле session.py:

from contextvars import ContextVar
from uuid import uuid4


class Session:
 """
 Сессия внешнего запроса.
 """

 def __init__(
 self,
 request_id: str,
 application_id: int,
 user_id: int
 ):
 self._request_id = request_id
 self._application_id = application_id
 self._user_id = user_id

 @property
 def request_id(self) -> str:
 return self._request_id

 @property
 def application_id(self) -> int:
 return self._application_id

 @application_id.setter
 def application_id(self, application_id: int) -> None:
 if application_id <= 0:
 raise ValueError(f'application_id must be positive integer, got {application_id}')
 self._application_id = application_id

 @property
 def user_id(self) -> int:
 return self._user_id

 @user_id.setter
 def user_id(self, user_id: int) -> None:
 if user_id <= 0:
 raise ValueError(f'user_id must be positive integer, got {user_id}')
 self._user_id = user_id

 def __repr__(self) -> str:
 return f'{self.__class__.__name__}({self.request_id}, {self.user_id})'


external_request_session: ContextVar[Session] = ContextVar(
 'external_request_session',
 default=Session(request_id=str(uuid4()), application_id=0, user_id=0)
)

В файле session_middleware.py:

from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from src.builtin_types import external_request_session
from .session import Session


class SessionMiddleware(BaseHTTPMiddleware):
 """
 Промежуточное программное обеспечение для работы с сессиями.
 """

 def __init__(self, app, application_id: int):
 super().__init__(app)
 self._application_id = application_id

 async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
 """
 Добавление сессии.

 :param request: Клиентский запрос.
 :param call_next: Функция обработки запроса.
 :return: Ответ сервера.
 """

 external_request_session.set(
 Session(
 request_id=str(uuid4()),
 application_id=self._application_id,
 user_id=0
 )
 )
 response = await call_next(request)

 return response

Вопрос 1: Объяснить, как работает и за что отвечает SessionMiddleware

2. Добавление логирования в приложение

Создаём новый пакет builtin_types/ в пакете src/, добавляем в него файл custom_logger.py и записываем следующий код:

from logging import DEBUG
from logging import Logger
from logging import getLogger
from logging.config import dictConfig
from typing import Optional

from .session import Session


class CustomLogger:
 """
 Логгер.
 """

 # Настройки логирования
 LOGGING_CONFIG = {
 'version': 1,
 'disable_existing_loggers': True,
 'formatters': {
 'standard': {
 'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
 },
 },
 'handlers': {
 'default': {
 'class': 'logging.StreamHandler',
 'formatter': 'standard',
 },
 },
 'loggers': {
 'uvicorn.error': {
 'level': 'INFO',
 'handlers': [
 'default',
 ],
 },
 'uvicorn.access': {
 'handlers': [
 'default',
 ],
 'level': 'INFO',
 'propagate': False,
 },
 'app': {
 'handlers': [
 'default',
 ],
 'level': 'INFO',
 'propagate': True
 },
 },
 }
 app_logger: Optional[Logger] = None

 @classmethod
 def init(cls, is_debug: bool = False) -> None:
 """
 Инициализация логгера.

 :param is_debug: Режим отладки.
 :return: None.
 """
 dictConfig(cls.LOGGING_CONFIG)
 cls.app_logger = getLogger('app')
 if is_debug:
 cls.app_logger.setLevel(DEBUG)
 getLogger('sqlalchemy.engine.Engine').disabled = not is_debug

 @classmethod
 def _get_session_log(cls, session: Session, message: str) -> str:
 """
 Сборка сообщения для сессионных логов.

 :param session: Сессия внешнего запроса.
 :param message: Сообщение.
 :return: Сообщение для сессии.
 """
 return f'User: {session.user_id} | Request: {session.request_id} | App: {session.application_id} | {message}'

 @classmethod
 def debug(cls, message: str) -> None:
 """
 Логирование отладочных сообщений.

 :param message: Сообщение.
 :return: None.
 """
 from src.builtin_types import external_request_session

 if cls.app_logger:
 session = external_request_session.get()
 if not session:
 cls.app_logger.debug(message)
 else:
 cls.app_logger.debug(cls._get_session_log(session=session, message=message))

 @classmethod
 def info(cls, message: str) -> None:
 """
 Логирование информационных сообщений.

 :param message: Сообщение.
 :return: None.
 """
 from src.builtin_types import external_request_session

 if cls.app_logger:
 session = external_request_session.get()
 if not session:
 cls.app_logger.info(message)
 else:
 cls.app_logger.info(cls._get_session_log(session=session, message=message))

 @classmethod
 def warning(cls, message: str) -> None:
 """
 Логирование предупреждений.

 :param message: Сообщение.
 :return: None.
 """
 from src.builtin_types import external_request_session

 if cls.app_logger:
 session = external_request_session.get()
 if not session:
 cls.app_logger.warning(message)
 else:
 cls.app_logger.warning(cls._get_session_log(session=session, message=message))

 @classmethod
 def error(cls, message: str) -> None:
 """
 Логирование ошибок.

 :param message: Сообщение.
 :return: None.
 """
 from src.builtin_types import external_request_session

 if cls.app_logger:
 session = external_request_session.get()
 if not session:
 cls.app_logger.error(message)
 else:
 cls.app_logger.error(cls._get_session_log(session=session, message=message))

Задание 1 – Добавить логирование в критические места приложения

3. Создание корневого приложения и монтируемых приложений FastAPI

Прежде чем реализовывать корневые и монтируемы приложения FastAPI, нам необходимо будет создать контроллер и репозиторий авторизации в Swagger.

В src/repositories создаём файл auth_repository.py и добавляем в него:

```
from aiohttp import ClientSession
from aiohttp import ClientTimeout
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

from src.builtin_types import CustomLogger
from src.enums import EncodingEnum
from src.exceptions import InvalidAccessTokenError
from src.exceptions import InvalidCredentialsError
from src.exceptions import InvalidTokenError
from src.exceptions import ValidationError
from src.interfaces.repositories import BaseRepositoryInterface
from src.schemas.responses import TokensResponse
from src.schemas.responses import VerifyAccessTokenResponse
from src.utils import CommonUtils
from src.utils import LoginRequestMapper
from src.utils import TokensResponseMapper
from src.utils import VerifyAccessTokenRequestMapper
from src.utils import VerifyAccessTokenResponseMapper


class AuthRepository(BaseRepositoryInterface):
 """
 Репозиторий для работы с авторизацией.
 """

 def __init__(self, auth_url: str):
 self._auth_url = auth_url

 self._login_by_userpass_endpoint = 'v1/authorization/login'
 self._verify_access_token_endpoint = 'v1/authentication/verify_access_token'

 async def login_by_userpass(
 self,
 form_data: OAuth2PasswordRequestForm,
 app_mount_path: str
 ) -> TokensResponse:
 async with ClientSession(
 base_url=CommonUtils.get_base_url(url=self._auth_url, mount_path=app_mount_path),
 timeout=ClientTimeout(total=10.0)
 ) as http_client:
 CustomLogger.debug(f'Send login request: {form_data.username}')

 login_request = await LoginRequestMapper.map_login_request(
 login=form_data.username,
 password=form_data.password
 )
 async with await http_client.post(
 url=self._login_by_userpass_endpoint,
 json=login_request.model_dump()
 ) as response:
 if response.status == status.HTTP_200_OK:
 CustomLogger.debug(f'Login request for {form_data.username} success')

 return await TokensResponseMapper.map_from_http_response(response=response)

 CustomLogger.error(f'Login request for {form_data.username} failed: {response.text}')

 raise InvalidCredentialsError()

 async def verify_access_token(self, access_token: str, app_mount_path: str) -> VerifyAccessTokenResponse:
 async with ClientSession(
 base_url=CommonUtils.get_base_url(url=self._auth_url, mount_path=app_mount_path),
 timeout=ClientTimeout(total=10.0)
 ) as async_http_client:
 CustomLogger.debug('Send verify access token request')

 verify_access_token_request = await VerifyAccessTokenRequestMapper.map_verify_access_token_request(
 access_token=access_token
 )
 async with await async_http_client.post(
 url=self._verify_access_token_endpoint,
 json=verify_access_token_request.model_dump()
 ) as response:
 if response.status == status.HTTP_401_UNAUTHORIZED:
 CustomLogger.error(f'Verify access token response: {response.text}')

 raise InvalidAccessTokenError()
 elif response.status == status.HTTP_400_BAD_REQUEST:
 CustomLogger.error(f'Verify access token response: {response.text}')

 raise InvalidTokenError()
 elif response.status == status.HTTP_422_UNPROCESSABLE_ENTITY:
 CustomLogger.error(f'Verify access token response: {response.text}')

 raise ValidationError(data=await response.json(encoding=EncodingEnum.UTF_8.value))

 CustomLogger.debug('Verify access token request success')

 return await VerifyAccessTokenResponseMapper.map_from_http_response(response=response)
```

Добавляем все недостающие классы и методы:

src/enums/encoding_enum.py

```
from enum import Enum


class EncodingEnum(str, Enum):
 """
 Перечисление кодировок.
 """

 UTF_8 = 'utf-8'
```

src/errors/validation_error.py

```
from http import HTTPStatus

from src.enums import MessageEnum
from src.schemas.common import BaseSchema
from .base_response_error import BaseResponseError


class ValidationError(BaseResponseError):
 """
 Ошибка валидации.
 """

 def __init__(self, data: BaseSchema):
 super().__init__(
 message=MessageEnum.VALIDATION_ERROR_MESSAGE,
 code=HTTPStatus.UNPROCESSABLE_ENTITY
 )
 self._data = data

 @property
 def data(self) -> BaseSchema:
 return self._data
```

Задание 2 – Добавить сообщение об ошибке валидации

src/utils/common_utils.py

```
from typing import Optional
from typing import Union
from urllib.parse import ParseResult
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse

from jose import jwt
from jose.exceptions import ExpiredSignatureError
from jose.exceptions import JWTError
from passlib.context import CryptContext

from settings import app_settings
from src.exceptions import ExpiredJwtTokenError
from src.exceptions import InvalidTokenError
from src.schemas.data_transfer_objects import AccessTokenFullDto
from src.schemas.data_transfer_objects import RefreshTokenFullDto
from src.schemas.data_transfer_objects import TokenDto
from .token_dto_mapper import TokenDtoMapper


class CommonUtils:
 """
 Базовые утилиты.
 """

 @staticmethod
 def create_jwt_token(token_dto: Union[AccessTokenFullDto, RefreshTokenFullDto]) -> str:
 """
 Создание JWT токена.

 :param token_dto: Сущность токена.
 :return: Токен.
 """

 token_dict = {
 'user': str(token_dto.user_id),
 'aud': str(token_dto.application_id),
 'exp': token_dto.expire_at.timestamp(),
 'iat': token_dto.created_at.timestamp(),
 'jti': str(token_dto.id),
 }
 return str(jwt.encode(token_dict, app_settings.SECRET_KEY, algorithm=app_settings.JWT_ALGORITHM))

 @staticmethod
 def decode_jwt_token(token: str) -> TokenDto:
 """
 Декодирование JWT токена.

 :param token: Токен.
 :return: Данные токена.
 :raise ExpiredJwtTokenError: Если срок действия токена истек.
 :raise InvalidTokenError: Если токен невалидный.
 """
 try:
 decoded_dict = jwt.decode(
 token=token,
 key=app_settings.SECRET_KEY,
 algorithms=[
 app_settings.JWT_ALGORITHM,
 ]
 )
 except ExpiredSignatureError:
 raise ExpiredJwtTokenError()
 except JWTError:
 raise InvalidTokenError()
 except Exception:
 raise
 return TokenDtoMapper.get_from_decoded_dict(decoded_dict=decoded_dict)

 @staticmethod
 def verify_password(plain_password: str, hashed_password: str, password_context: CryptContext) -> bool:
 """
 Проверка пароля.

 :param plain_password: Незашифрованный пароль.
 :param hashed_password: Зашифрованный пароль.
 :param password_context: Контекст хэширования.
 :return: Результат проверки пароля.
 """

 return bool(password_context.verify(plain_password, hashed_password))

 @staticmethod
 def check_trail_slash(path: str) -> str:
 """
 Проверка пути на закрывающий слэш.

 :param path: Путь.
 :return: Путь.
 """
 if not path.endswith('/'):
 path += '/'

 return path

 @classmethod
 def get_base_url(cls, url: str, mount_path: Optional[str] = None) -> str:
 """
 Получение корневого URL.

 :param url: URL.
 :param mount_path: Наименование монтируемого приложения.
 :return: Корневой URL.
 """
 parsed_base_url: ParseResult = urlparse(url=url)
 path = parsed_base_url.path
 if mount_path:
 path = urljoin(base=cls.check_trail_slash(parsed_base_url.path), url=f'.{mount_path}')

 result_base_url: str = urlunparse(
 (
 parsed_base_url.scheme,
 parsed_base_url.netloc,
 cls.check_trail_slash(path=path),
 parsed_base_url.params,
 parsed_base_url.query,
 parsed_base_url.fragment
 )
 )

 return result_base_url
```

src/utils/login_request_mapper.py

```
from src.schemas.requests import LoginRequestSchema


class LoginRequestMapper:
 """
 Сборка запроса для входа в систему.
 """

 @staticmethod
 async def map_login_request(login: str, password: str) -> LoginRequestSchema:
 """
 Сборка схемы запроса для входа в систему.

 :param login: Логин пользователя.
 :param password: Пароль пользователя.
 :return: Запрос для входа в систему.
 """
 return LoginRequestSchema(login=login, password=password)
```

src/utils/token_response_mapper.py

```
from aiohttp import ClientResponse

from src.schemas.responses import TokensResponse


class TokensResponseMapper:
 """
 Сборка схемы ответа на создание/обновление токенов.
 """

 @staticmethod
 def map_tokens_response(
 access_token: str,
 refresh_token: str
 ) -> TokensResponse:
 """
 Сборка схемы ответа на создание/обновление токенов.

 :param access_token: Токен доступа
 :param refresh_token: Токен обновления
 :return: Схема ответа на создание/обновление токенов
 """

 return TokensResponse(access_token=access_token, refresh_token=refresh_token)

 @staticmethod
 async def map_from_http_response(response: ClientResponse) -> TokensResponse:
 """
 Сборка схемы ответа на создание/обновление токенов из HTTP-ответа.

 :param response: HTTP-ответ.
 :return: Схема ответа на создание/обновление токенов.
 """
 data = await response.json()
 return TokensResponse.model_construct(**data)
```

src/utils/verify_access_token_request_mapper

```
from src.schemas.requests import VerifyAccessTokenRequest


class VerifyAccessTokenRequestMapper:
 """
 Сборка запроса для проверки access-токена.
 """

 @staticmethod
 async def map_verify_access_token_request(access_token: str) -> VerifyAccessTokenRequest:
 """
 Сборка схемы запроса для проверки access-токена.

 :param access_token: Access-токен.
 :return: Запрос для проверки access-токена.
 """
 return VerifyAccessTokenRequest(access_token=access_token)
```

Далее, можем наконец добавить контроллер

```
from typing import Dict

from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

from src.builtin_types import CustomLogger
from src.exceptions import BaseCustomError
from src.interfaces.controllers import BaseControllerInterface
from src.repositories import AuthRepository
from src.schemas.responses import VerifyAccessTokenResponse


class AuthController(BaseControllerInterface):
 """
 Контроллер авторизации и аутентификации.
 """

 def __init__(self, authentication_repository: AuthRepository):
 self._auth_repository = authentication_repository

 async def login_by_userpass_in_swagger(
 self,
 form_data: OAuth2PasswordRequestForm,
 app_mount_path: str,
 ) -> Dict[str, str]:
 """
 Авторизация по логину и паролю.

 :param form_data: Данные формы авторизации в Swagger.
 :param app_mount_path: Путь монтирования приложения.
 :return: Словарь с access-токеном.
 :raise HTTPException: Если авторизация не удалась.
 """
 CustomLogger.info(message=f'Send login request, app_mount_path: {app_mount_path}')

 try:
 tokens_response = await self._auth_repository.login_by_userpass(
 form_data=form_data,
 app_mount_path=app_mount_path
 )
 CustomLogger.info(message=f'Login request success, app_mount_path: {app_mount_path}')

 return {
 'access_token': tokens_response.access_token,
 'token_type': 'bearer',
 }

 except BaseCustomError as exc:
 CustomLogger.error(message=f'Login request failed: {exc}')

 raise HTTPException(
 status_code=status.HTTP_401_UNAUTHORIZED,
 detail='Invalid authentication credentials',
 headers={
 'WWW-Authenticate': 'Bearer',
 },
 )

 async def verify_access_token(self, access_token: str, app_mount_path: str) -> VerifyAccessTokenResponse:
 """
 Проверка access-токена.

 :param access_token: Access-токен для проверки.
 :param app_mount_path: Путь монтирования приложения.
 :return: Информация о сессии.
 :raise InvalidAccessTokenError: Если access-токен недействителен.
 """
 CustomLogger.info(message=f'Send verify access token request, app_mount_path: {app_mount_path}')

 try:
 verify_access_token_response = await self._auth_repository.verify_access_token(
 access_token=access_token,
 app_mount_path=app_mount_path
 )
 CustomLogger.info(message=f'Verify access token request success, app_mount_path: {app_mount_path}')

 return verify_access_token_response

 except BaseCustomError as exc:
 CustomLogger.error(message=f'Verify access token request failed: {exc}')

 raise exc
```

Создаём кастомный роутер в src/routers:

```
from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi.params import Depends


class CustomRouter:
 """
 Кастомизированный HTTP API роутер.
 """

 def __init__(
 self,
 router_prefix: str,
 name: str,
 description: str,
 has_authentication: bool = True,
 dependencies: Optional[List[Depends]] = None,
 deprecated: Optional[bool] = None,
 include_in_schema: bool = True
 ):
 """
 :param router_prefix: Префикс путей роутера. Пример: /items.
 :param name: Название роутера на английском. Пример: Items.
 :param description: Описание роутера. Пример: Работа с объектами.
 :param has_authentication: Имеет ли роутер аутентификацию.
 :param dependencies: Список глобальных зависимостей роутера.
 :param deprecated: Роутер устарел.
 :param include_in_schema: Включить ли в схему.
 """
 self._name = name
 self._description = description
 self._has_authentication = has_authentication
 self._deprecated = deprecated
 self._include_in_schema = include_in_schema

 if not dependencies:
 dependencies = list()
 self._api_router = APIRouter(
 prefix=router_prefix,
 dependencies=dependencies,
 deprecated=self._deprecated,
 include_in_schema=self._include_in_schema
 )

 @property
 def name(self) -> str:
 return self._name

 @property
 def description(self) -> str:
 return self._description

 @property
 def has_authentication(self) -> bool:
 return self._has_authentication

 @property
 def api_router(self) -> APIRouter:
 return self._api_router

 def __str__(self) -> str:
 return f'{self._name} - {self._description}'

 def __repr__(self) -> str:
 return self.__str__()
```

Задание 3 – Использовать кастомный роутер вместо APIRouter в уже созданных роутерах

Создаём пакет application/ в пакете src/, и добавляем туда 2 файла: root_application.py и mounted_application.py

В файле mounted_application.py:

```
from typing import Dict
from typing import List
from typing import Optional

from fastapi import Depends
from fastapi import FastAPI
from fastapi import status
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from pydantic import ValidationError as PydanticValidationError

from settings import app_settings
from src.builtin_types import SessionMiddleware
from src.controllers import AuthController
from src.exceptions import BaseResponseError
from src.repositories import AuthRepository
from src.routers import CustomRouter
from src.utils import JsonResponseMapper
from src.utils import SessionManager


class MountedApplication:
 """
 Монтируемое FastAPI приложение.
 """
 SWAGGER_ROUTER_PREFIX = '/swagger'
 SWAGGER_LOGIN_PATH = '/login'

 def __init__(
 self,
 *,
 swagger_title_prefix: str,
 routers: Dict[int, List[CustomRouter]],
 application_id: int,
 mount_path: str,
 middleware: Optional[List[Middleware]] = None
 ):
 """
 :param swagger_title_prefix: Префикс названия приложения.
 :param routers: Словарь роутеров. Ключ - версия API, значение - список роутеров.
 :param application_id: Идентификатор приложения.
 :param mount_path: Путь монтируемого приложения.
 :param middleware: Список дополнительных middleware.
 """
 self._title = f'{swagger_title_prefix} {app_settings.SWAGGER_TITLE}'
 self._version = app_settings.APP_VERSION
 self._routers = routers
 self._middleware = list()
 self._application_id = application_id
 self._mount_path = mount_path
 self._oauth2_scheme = OAuth2PasswordBearer(
 tokenUrl=f'{app_settings.ROOT_PATH}{self._mount_path}{self.SWAGGER_ROUTER_PREFIX}{self.SWAGGER_LOGIN_PATH}'
 )

 self._middleware.append(
 Middleware(
 CORSMiddleware,
 allow_origins=['*'],
 allow_methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
 allow_headers=[
 'X-CSRF-Token',
 'X-Requested-With',
 'Accept',
 'Accept-Version',
 'Content-Length',
 'Content-MD5',
 'Content-Type',
 'Date',
 'X-Api-Version',
 'Authorization',
 'api-key',
 ],
 allow_credentials=True,
 expose_headers=['*'],
 max_age=31536000
 )
 )
 self._middleware.append(
 Middleware(
 SessionMiddleware, # noqa
 application_id=self._application_id
 )
 )
 if middleware:
 self._middleware.extend(middleware)

 # Создание роутера для авторизации в Swagger
 self._swagger_authentication_router = CustomRouter(
 router_prefix=self.SWAGGER_ROUTER_PREFIX,
 name='Swagger',
 description='Авторизация для Swagger',
 has_authentication=False,
 include_in_schema=False
 )

 @self._swagger_authentication_router.api_router.post(
 path=self.SWAGGER_LOGIN_PATH,
 summary='Авторизация Swagger',
 response_model=Dict[str, str],
 status_code=status.HTTP_200_OK,
 responses={
 status.HTTP_200_OK: {
 'access_token': 'eyJhbGciOiJIUz.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZS.SflKxwRJSMeKKF2QT4fwp',
 'token_type': 'bearer',
 },
 }
 )
 async def login(
 form_data: OAuth2PasswordRequestForm = Depends(),
 auth_controller: AuthController = Depends(self._authentication_controller)
 ) -> Dict[str, str]:
 return await auth_controller.login_by_userpass_in_swagger(
 form_data=form_data,
 app_mount_path=self._mount_path
 )

 @property
 def title(self) -> str:
 """
 Возвращает название приложения.

 :return: Название приложения.
 """

 return self._title

 @property
 def mount_path(self) -> str:
 """
 Возвращает монтируемый путь.

 :return: Монтируемый путь.
 """
 return self._mount_path

 @classmethod
 async def _authentication_controller(cls, _: Request) -> AuthController:
 """
 Зависимость с контроллером авторизации и аутентификации.

 :param _: Внешний запрос.
 :return: Контроллер аутентификации.
 """
 return AuthController(authentication_repository=AuthRepository(auth_url=app_settings.AUTH_URL))

 def create_app(self) -> FastAPI:
 """
 Создание экземпляра монтируемого приложения.

 :return: Экземпляр монтируемого приложения.
 """
 openapi_tags = list()

 for routers in self._routers.values():
 for router in routers:
 openapi_tags.append(
 {
 'name': router.name,
 'description': router.description,
 }
 )
 application = FastAPI(
 title=self._title,
 openapi_tags=openapi_tags,
 version=self._version,
 middleware=self._middleware,
 redirect_slashes=False,
 docs_url='/docs'
 )

 @application.exception_handler(BaseResponseError)
 async def handle_base_response_error(_: Request, exception: BaseResponseError) -> JSONResponse:
 """
 Обработка ошибок без данных.

 :param _: Запрос.
 :param exception: Объект исключения без данных.
 :return: Ответ с сообщением об ошибке.
 """

 return await JsonResponseMapper.get_from_base_response_error(
 exception=exception,
 message=str(exception.message.value)
 )

 @application.exception_handler(PydanticValidationError)
 async def handle_validation_error(_: Request, exception: PydanticValidationError) -> JSONResponse:
 """
 Обработка ошибок валидации Pydantic.

 :param _: Внешний запрос.
 :param exception: Объект исключения валидации Pydantic.
 :return: Ответ с сообщением об ошибке.
 """
 return await JsonResponseMapper.get_from_pydantic_validation_error(pydantic_validation_error=exception)

 @application.exception_handler(Exception)
 async def handle_exception(_: Request, exception: Exception) -> JSONResponse:
 """
 Обработка внештатных исключений.

 :param _: Запрос.
 :param exception: Объект исключения.
 :return: Ответ с сообщением об ошибке.
 """
 return await JsonResponseMapper.get_from_exception(exception=exception)

 async def _get_session(
 _: Request,
 access_token: str = Depends(self._oauth2_scheme),
 auth_controller: AuthController = Depends(self._authentication_controller)
 ) -> None:
 """
 Зависимость с аутентификацией пользователя при обработке внешних запросов.

 :param _: Внешний запрос.
 :param access_token: Токен доступа.
 :param auth_controller: Контроллер авторизации и аутентификации.
 :return: None.
 """
 access_token_response = await auth_controller.verify_access_token(
 access_token=access_token,
 app_mount_path=self._mount_path
 )
 SessionManager.update_user_id(user_id=access_token_response.session.user_id)

 for api_version, routers in self._routers.items():
 if api_version < 0:
 raise ValueError(f'Invalid api version: {api_version}')
 for router in routers:
 prefix = f'/v{api_version}' if api_version > 0 else ''
 if router.has_authentication:
 application.include_router(
 router.api_router,
 prefix=prefix,
 tags=[router.name],
 dependencies=[Depends(_get_session)]
 )
 else:
 application.include_router(router.api_router, prefix=prefix, tags=[router.name])
 application.include_router(
 self._swagger_authentication_router.api_router,
 tags=[self._swagger_authentication_router.name]
 )

 return application
```

В файле root_application.py:

```
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from typing import List
from urllib.parse import urlparse

from fastapi import FastAPI
from fastapi.routing import Mount
from ping3 import ping # type: ignore[import-untyped]

from settings import app_settings
from src.builtin_types import CustomLogger
from .mounted_application import MountedApplication


class RootApplication:
 """
 Корневое FastAPI приложение.
 """

 def __init__(
 self,
 *,
 mounted_applications: List[MountedApplication]
 ):
 """
 :param mounted_applications: Монтируемые приложения. Ключ - путь, значение - монтируемое приложение.
 """
 self._mounted_applications = mounted_applications

 @classmethod
 def _ping_host(cls, full_url: str) -> bool:
 """
 Проверка доступности хоста.

 :param full_url: Полный адрес хоста.
 :return: Результат пинга.
 """
 CustomLogger.info(message=f'Ping host: {full_url}')

 host = urlparse(full_url).hostname
 result = ping(host)

 if isinstance(result, float):
 return True
 return False

 @asynccontextmanager
 async def _lifespan(self, application: FastAPI) -> AsyncGenerator[None, None]:
 """
 Жизненный цикл приложения.

 :param application: Экземпляр приложения.
 :return: None.
 """
 # Инициализация логгера
 CustomLogger.init(is_debug=app_settings.IS_DEBUG)

 CustomLogger.info('Start root application')

 # Перечисление примонтированных приложений
 for route in application.routes:
 if isinstance(route, Mount):
 CustomLogger.info(f'Mounted application: {route.name} {route.path}')

 yield

 CustomLogger.info('Stop root application')

 def create_app(self) -> FastAPI:
 """
 Создание экземпляра корневого приложения.

 :return: Экземпляр корневого приложения.
 """

 application = FastAPI(
 title=app_settings.SWAGGER_TITLE,
 version=app_settings.APP_VERSION,
 root_path=app_settings.ROOT_PATH,
 lifespan=self._lifespan,
 redirect_slashes=False
 )
 for mounted_application in self._mounted_applications:
 mounted_fast_api_instance = mounted_application.create_app()
 application.mount(
 path=mounted_application.mount_path,
 app=mounted_fast_api_instance,
 name=mounted_application.title
 )

 return application
```

Задание 4 – Разобраться в логике работы корневого и понтируемых приложений

Переходим в основной файл приложения main.py и изменияем его содержимое:

```
from fastapi import FastAPI
from uvicorn import run

from settings import app_settings
from src.application import MountedApplication
from src.application import RootApplication
from src.builtin_types import CustomLogger
from src.enums import ApplicationEnum
from src.routers import web_authentication_router
from src.routers import web_authorization_router
from src.routers import web_post_router

app = FastAPI()

web_application = MountedApplication(
 swagger_title_prefix='Web',
 routers={
 0: [],
 1: [
 web_post_router,
 web_authorization_router,
 web_authentication_router,
 ],
 2: [],
 },
 application_id=ApplicationEnum.web.value,
 mount_path='/web'
)
admin_application = MountedApplication(
 swagger_title_prefix='Admin',
 routers={
 0: [],
 1: [],
 2: [],
 },
 application_id=ApplicationEnum.admin.value,
 mount_path='/admin'
)

main_application = RootApplication(
 mounted_applications=[
 admin_application,
 web_application,
 ]
)

application = main_application.create_app()


def main():
 """
 Запуск тестового сервера.
 """
 try:
 CustomLogger.info('Start FastAPI application')
 run(
 application,
 host=app_settings.HOST,
 port=app_settings.PORT,
 log_config=CustomLogger.LOGGING_CONFIG
 )
 except Exception as e:
 CustomLogger.error(f'❌ FastAPI start filed: {e}')


if __name__ == '__main__':
 main()
```

Теперь необходимо обновить настройки приложения и добавить переменные окружения:

```
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AppSettings(BaseSettings):
 """
 Настройки приложения.
 """

 model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

 APP: str = 'main:app'
 HOST: str = '0.0.0.0'
 PORT: int = 8000
 SWAGGER_TITLE: str = 'Blog API'
 APP_VERSION: str = '0.0.0'
 ROOT_PATH: str = ''
 IS_DEBUG: bool = False

 SQL_DSN: str = 'postgresql+asyncpg://user:password@localhost:5432/db'
 USERS_SQL_SCHEMA: str = 'users'
 POSTS_SQL_SCHEMA: str = 'posts'

 SECRET_KEY: str = 'very_secret_64_chars_hash'
 JWT_ALGORITHM: str = 'HS256'
 ACCESS_TOKEN_EXPIRES_MINUTES: int = 60
 REFRESH_TOKEN_EXPIRES_MINUTES: int = 43200

app_settings = AppSettings()
```

Задание 5 – обновить переменные окружения в .env самостоятельно

4. Админ-панель

После создание класса монтируемых приложения, мы можем с лёгкостью разделять приложения на клиентские (web) и админские (admin).

Для админ-панели нам понадобятся отдельные роутеры с префиксом admin_

Создадим админский роутер для пользователей

src/routers/admin_user_router

```
from typing import Annotated
from typing import List

from fastapi import Depends
from fastapi import Path
from fastapi import status

from src.controllers import UserController
from src.dependencies import get_user_controller
from src.schemas.data_transfer_objects import UserFullDto
from .custom_router import CustomRouter

admin_user_router = CustomRouter(
 router_prefix='/user',
 name='Пользователя',
 description='Методы для работы с пользователями в админ-панели',
 deprecated=False,
 has_authentication=False
)


@admin_user_router.api_router.put(
 path='',
 description='Создание/обновления пользователя',
 summary='Создание/обновление пользователя',
 response_model=UserFullDto,
 status_code=status.HTTP_201_CREATED
)
async def upsert(
 user_dto: UserFullDto,
 user_controller: Annotated[UserController, Depends(get_user_controller)]
) -> UserFullDto:
 """
 Создание/обновления пользователя.
 """

 return await user_controller.upsert(user_full_dto=user_dto)


@admin_user_router.api_router.put(
 path='/many',
 description='Создание/обновления списка пользователей',
 summary='Создание/обновления списка пользователей',
 response_model=List[UserFullDto],
 status_code=status.HTTP_201_CREATED
)
async def upsert_many(
 user_dto_list: List[UserFullDto],
 user_controller: Annotated[UserController, Depends(get_user_controller)]
) -> List[UserFullDto]:
 """
 Создание/обновления списка пользователей.
 """

 return await user_controller.upsert_many(user_dto_list=user_dto_list)


@admin_user_router.api_router.get(
 path='/many',
 description='Получение списка пользователей',
 summary='Получение списка пользователей',
 response_model=List[UserFullDto],
 status_code=status.HTTP_200_OK
)
async def get_many(
 user_controller: Annotated[UserController, Depends(get_user_controller)]
) -> List[UserFullDto]:
 """
 Получение списка пользователей.
 """

 return await user_controller.get_all()


@admin_user_router.api_router.get(
 path='/{userId}',
 description='Получение пользователя',
 summary='Получение пользователя',
 response_model=UserFullDto,
 status_code=status.HTTP_200_OK
)
async def get_one(
 user_controller: Annotated[UserController, Depends(get_user_controller)],
 user_id: int = Path(
 description='ID пользователя',
 alias='userId',
 ge=1,
 example=1
 )
) -> UserFullDto:
 """
 Получение пользователя.
 """

 return await user_controller.get_one(user_id=user_id)


@admin_user_router.api_router.delete(
 path='/{userId}',
 description='Удаление пользователя',
 summary='Удаление пользователя',
 response_model=None,
 status_code=status.HTTP_204_NO_CONTENT
)
async def delete_one(
 user_controller: Annotated[UserController, Depends(get_user_controller)],
 user_id: int = Path(
 description='ID пользователя',
 alias='userId',
 ge=1,
 example=1
 )
) -> None:
 """
 Удаление пользователя.
 """

 return await user_controller.delete(user_id=user_id)
```

Задание 6 – Создать контроллер пользователей с указанными в конечных точках методами

Внедрение админского роутера пользователей в приложение:

main.py

```
from fastapi import FastAPI
from uvicorn import run

from settings import app_settings
from src.application import MountedApplication
from src.application import RootApplication
from src.builtin_types import CustomLogger
from src.enums import ApplicationEnum
from src.routers import admin_user_router
from src.routers import web_authentication_router
from src.routers import web_authorization_router
from src.routers import web_post_router

app = FastAPI()

web_application = MountedApplication(
 swagger_title_prefix='Web',
 routers={
 0: [],
 1: [
 web_post_router,
 web_authorization_router,
 web_authentication_router,
 ],
 2: [],
 },
 application_id=ApplicationEnum.web.value,
 mount_path='/web'
)
admin_application = MountedApplication(
 swagger_title_prefix='Admin',
 routers={
 0: [],
 1: [
 admin_user_router,
 ],
 2: [],
 },
 application_id=ApplicationEnum.admin.value,
 mount_path='/admin'
)

main_application = RootApplication(
 mounted_applications=[
 admin_application,
 web_application,
 ]
)

application = main_application.create_app()


def main():
 """
 Запуск тестового сервера.
 """
 try:
 CustomLogger.info('Start FastAPI application')
 run(
 application,
 host=app_settings.HOST,
 port=app_settings.PORT,
 log_config=CustomLogger.LOGGING_CONFIG
 )
 except Exception as e:
 CustomLogger.error(f'❌ FastAPI start filed: {e}')


if __name__ == '__main__':
 main()
```

ЗАДАНИЯ

- Создать ветку feature/lab5 от develop

- Внедрить Swagger аутентификацию для конечных точек

- Создать контроллер для работы с пользователями

- Запустить контейнер с серверным приложением и проверить корректность работы конечных точек

- Записать ответы на все вопросы в основной части в CHANGELOG.md

- Запушить ветку в удалённый репозиторий и создать Merge Request

ЛАБОРАТОРНАЯ РАБОТА 6

ФОНОВЫЕ ЗАДАЧИ И ИСПОЛЬЗОВАНИЕ SMTP ПРОТОКОЛА

Цель работы: Реализовать асинхронные фоновые задачи и отправку сообщений на почту с использованием SMTP протокола.

ВВЕДЕНИЕ

Фоновые задачи в FastAPI

Фоновые задачи (Background Tasks) в FastAPI — это механизм для выполнения операций, которые должны произойти после отправки ответа клиенту. Это позволяет не задерживать ответ, если какие-то действия (например, отправка email, обработка данных, логирование) требуют времени, но не являются критичными для немедленного возврата результата пользователю.

Принцип работы

Когда вы определяете фоновую задачу, FastAPI добавляет её в очередь. После формирования основного ответа (например, JSON-данных) и его отправки клиенту, приложение приступает к выполнению задач из этой очереди. Клиент не ждет завершения этих задач, что значительно сокращает время отклика API.

Типичные сценарии использования:

- Отправка уведомлений: Email, SMS, push-сообщения.

- Обработка данных: Генерация отчетов, конвертация файлов, анализ загруженной информации.

- Ведение логов и аналитики: Запись действий пользователя, обновление счетчиков.

- Интеграции со сторонними сервисами: Вызов внешних API, где задержка не важна для основного потока.

- Очистка и обслуживание: Удаление временных файлов, обновление кэшей.

Важные аспекты:

- Отказоустойчивость: Если фоновая задача завершится с ошибкой, основной ответ клиенту уже будет отправлен и не пострадает. Однако это означает, что логику фоновых задач нужно проектировать с учетом возможных сбоев и механизмов повтора.

- Производительность: Задачи выполняются в том же процессе, что и основное приложение (если не используется отдельный воркер). Долгие или блокирующие задачи могут повлиять на общую производительность сервера.

- Для сложных сценариев: Встроенный механизм фоновых задач FastAPI идеален для простых операций. Для сложных распределенных задач, требующих очереди, планирования, повтора и масштабирования, следует использовать специализированные системы (Celery, RQ, ARQ).

Протокол SMTP для отправки электронной почты

SMTP (Simple Mail Transfer Protocol) — это коммуникационный протокол прикладного уровня, предназначенный для передачи электронной почты в сетях TCP/IP. Он определяет правила диалога между почтовыми клиентами (отправителями) и серверами, а также между самими серверами.

Ключевые компоненты

- SMTP-клиент (MUA - Mail User Agent): Программа, с которой взаимодействует пользователь (например, почтовое приложение или ваше веб-приложение FastAPI), чтобы инициировать отправку письма.

- SMTP-сервер (MTA - Mail Transfer Agent): Программное обеспечение, которое получает, обрабатывает, перенаправляет и доставляет почту. Примеры: Postfix, Exim, Microsoft Exchange, а также публичные сервисы (SMTP-сервер Gmail, Mail.ru, Yandex).

- Порт: По умолчанию SMTP использует порт 25. Для безопасного соединения используются порты 465 (SMTP over SSL, устаревший, но распространенный) и 587 (для начала незашифрованного соединения с последующим обязательным переходом на шифрование по команде STARTTLS).

Этапы отправки письма (упрощенно)

- Подготовка письма: Клиент формирует сообщение, включая заголовки (From, To, Subject, Date) и тело письма.

- Установка соединения: Клиент устанавливает TCP-соединение с SMTP-сервером отправителя (или релеем).

- Квитирование (Handshake): Сервер подтверждает готовность. Клиент и сервер представляются.

- Идентификация (аутентификация): В современных реалиях клиент обычно аутентифицируется на сервере с помощью логина и пароля (например, по механизмам LOGIN, PLAIN или CRAM-MD5), чтобы доказать право на отправку писем (во избежание спама).

- Передача данных:

  - Клиент указывает адрес отправителя (MAIL FROM).

  - Клиент указывает адрес(а) получателя (RCPT TO).

  - Клиент передает само содержимое письма (DATA), включая заголовки и тело.

- Завершение: Клиент инициирует завершение сеанса (QUIT).

- Маршрутизация: Если получатель находится в другом почтовом домене, SMTP-сервер отправителя выступает в роли клиента и повторяет процесс, соединяясь с SMTP-сервером получателя, чтобы передать ему письмо для конечной доставки.

Безопасность (SMTPs, STARTTLS)

- SMTPs (SMTPS): Изначально зашифрованное соединение по SSL/TLS (часто на порту 465). Вся сессия шифруется.

- STARTTLS: Команда, которая "обновляет" изначально незашифрованное соединение (например, на порту 587) до защищенного TLS-соединения. Это предпочтительный современный метод, так как он позволяет использовать один порт как для защищенной, так и (в случае проблем) для незащищенной передачи, но при этом требует обязательного перехода на шифрование.

ОСНОВНАЯ ЧАСТЬ

1. Создание SMTP репозитория

Обновлённый файл настроек settings.py:

```
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AppSettings(BaseSettings):
 """
 Настройки приложения.
 """

 model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

 APP: str = 'main:app'
 HOST: str = '0.0.0.0'
 PORT: int = 8000
 SWAGGER_TITLE: str = 'Blog API'
 APP_VERSION: str = '0.0.0'
 ROOT_PATH: str = ''
 IS_DEBUG: bool = False
 STATIC_PATH: str = 'src/static'

 AUTH_URL: str = 'http://localhost:8000'

 SQL_DSN: str = 'postgresql+asyncpg://user:password@localhost:5432/db'
 USERS_SQL_SCHEMA: str = 'users'
 POSTS_SQL_SCHEMA: str = 'posts'

 SECRET_KEY: str = 'very_secret_64_chars_hash'
 JWT_ALGORITHM: str = 'HS256'
 ACCESS_TOKEN_EXPIRES_MINUTES: int = 60
 REFRESH_TOKEN_EXPIRES_MINUTES: int = 43200

 # SMTP
 SMTP_HOST: str = 'example.mail.com'
 SMTP_PORT: int = 587
 SMTP_USER: str = 'example@gmail.com'
 SMTP_PASSWORD: str = "chan geme pass word"
 SMTP_TIMEOUT: int = 10
 SMTP_USE_TLS: bool = False
 SMTP_START_TLS: bool = True
 SMTP_ALLOWED_SENDER_DOMAINS: str = 'example.com'
 IS_NEED_SEND_EMAIL: bool = True # Feature flag


app_settings = AppSettings()
```

В src/repositories создаём файл smtp_repository.py и записываем следующий код:

```
from email.message import EmailMessage
from typing import Any
from typing import Callable
from typing import Coroutine

from aiosmtplib import SMTP
from aiosmtplib import SMTPException

from src.builtin_types import CustomLogger
from src.interfaces.repositories import BaseRepositoryInterface


def smtp_exception_handler(
 method: Callable[..., Coroutine[Any, Any, Any]]
) -> Callable[..., Coroutine[Any, Any, Any]]:
 """
 Декоратор для обработки SMTP ошибок.

 :param method: Декорируемый метод.
 :return: Декорированный метод.
 """

 async def wrapper(*args, **kwargs) -> Any:
 try:
 return await method(*args, **kwargs)
 except SMTPException as exc:
 CustomLogger.error(f'SMTP unexpected error: {exc}')

 raise exc

 return wrapper


class SMTPRepository(BaseRepositoryInterface):
 """
 Репозиторий для работы с SMTP.
 """

 def __init__(self, smtp_session: SMTP, is_need_send_email: bool) -> None:
 self._smtp_session = smtp_session
 self._is_need_send_email = is_need_send_email

 @smtp_exception_handler
 async def send_message(self, email_message: EmailMessage) -> None:
 """
 Отправка сообщения на почту.

 :param email_message: Сообщения для пользователя
 :return: None.
 """
 if self._is_need_send_email:
 CustomLogger.debug(f'Send email to: {email_message["To"]}')

 await self._smtp_session.send_message(email_message)
```

Вопрос 1 – Объяснить значение параметра is_need_send_email в классе SMTPRepository. Можно ли убрать этот флаг, и как программа будет вести себя в дальнейшем без него?

Для хранения предметов почтовых сообщений создадим отдельное перечисление в src/enums

email_subject_enum.py

```
from enum import Enum


class EmailSubjectEnum(str, Enum):
 """
 Перечисление предметов почтовых сообщений.
 """

 SUCCESS_LOGIN_SUBJECT = 'Успешный вход в приложение'
```

2. Создание репозитория для работы с файлами в памяти

Содержание сообщения для отправки на почту формируется из файла разметки *.html. Создадим папку static в пакете src/ и добавим туда файл success_login_template.html со следующим содержанием (можно использовать свой вариант):

```
<p>Добрый день, {username}!</p><br>
<p>Вы успешно вошли в свой аккаунт в приложении "Блог".</p><br>
<p>Теперь вы можете создавать новые записи, комментировать статьи других авторов и управлять своим профилем.</p><br>
<p>Если это были не вы, пожалуйста, немедленно свяжитесь со службой поддержки.</p><br>
<p>С уважением,<br>Команда Блога</p>
```

Для работы с файлами в памяти создадим отдельный репозиторий в src/repositories

static_files_repository.py

```
from pathlib import Path

from aiofile import async_open

from src.builtin_types import CustomLogger
from src.interfaces.repositories import BaseRepositoryInterface


class StaticFilesRepository(BaseRepositoryInterface):
 """
 Репозиторий для работы с файлами в памяти.
 """

 def __init__(self, static_path: str) -> None:
 self._static_path = static_path

 async def get_file_as_bytes(self, file_name: str) -> bytes:
 """
 Чтение файла как набора байт.

 :param file_name: Имя файла.
 :return: Файл в виде строки байтов.
 """
 CustomLogger.debug(f'Get static file as bytes: {file_name}')

 file_path: Path = Path(self._static_path).joinpath(file_name)
 async with await async_open(file_specifier=file_path, mode='rb') as f:
 return bytes(await f.read())
```

Для хранения названий файлов в памяти создадим отдельное перечисление в src/enums

static_file_name_enum.py

```
from enum import Enum


class StaticFileNameEnum(str, Enum):
 """
 Перечисление названий файлов в памяти.
 """

 SUCCESS_LOGIN_TEMPLATE = 'success_login_template.html'
```

3. Контроллер для работы с SMTP

Определим отдельный контроллер для работы с почтовым сервисом, для этого в src/controllers создадим файл smtp_controller.py и вставим следующий код:

```
from src.builtin_types import CustomLogger
from src.enums import StaticFileNameEnum
from src.interfaces.controllers import BaseControllerInterface
from src.repositories import SMTPRepository
from src.repositories import StaticFilesRepository
from src.utils import CommonUtils


class SMTPController(BaseControllerInterface):
 """
 Контроллер для работы с SMTP.
 """

 def __init__(self, smtp_repository: SMTPRepository, static_files_repository: StaticFilesRepository) -> None:
 self._smtp_repository = smtp_repository
 self._static_files_repository = static_files_repository

 async def send_login_message(self, email_to: str, username: str) -> None:
 """
 Отправка сообщений об успешном входе в приложение.

 :param email_to: Почта адресата.
 :param username: Имя пользователя.
 :return: None.
 """
 CustomLogger.info(f'Send login email to: {email_to}')

 await self._smtp_repository.send_message(
 email_message=CommonUtils.get_login_email_message(
 email_to=email_to,
 username=username,
 email_message_content=await self._static_files_repository.get_file_as_bytes(
 file_name=StaticFileNameEnum.SUCCESS_LOGIN_TEMPLATE.value
 )
 )
 )
```

Вопрос 2 – Зачем нужен отдельный контроллер для работы с почтовым сервисом? Можем ли мы использовать SMTP репозиторий в UserController или PostController, если нам понадобится отправка сообщения?

Для CommonUtils добавим:

```
@staticmethod
def build_email_message(
 email_to: str,
 email_message_content_string: str,
 subject: EmailSubjectEnum
) -> EmailMessage:
 """
 Сборка сообщения для отправки на почту.

 :param email_to: Почта пользователя.
 :param email_message_content_string: Шаблон сообщения.
 :param subject: Предмет сообщения.
 :return: Сообщение для отправки на почту.
 """

 email_message = EmailMessage()
 email_message['From'] = app_settings.SMTP_USER
 email_message['To'] = email_to
 email_message['Subject'] = subject.value
 email_message.set_content(email_message_content_string, subtype='html')

 return email_message

@classmethod
def get_login_email_message(
 cls,
 email_to: str,
 username: str,
 email_message_content: bytes
) -> EmailMessage:
 """
 Генерация сообщения об успешном входе для отправки на почту.

 :param email_to: Почта адресата.
 :param username: Имя пользователя.
 :param email_message_content: Содержание почтового сообщения.
 :return: Сообщение для отправки на почту.
 """
 email_message_content_string: str = email_message_content.decode(encoding=EncodingEnum.UTF_8.value).format(
 username=username
 )

 return cls.build_email_message(
 email_to=email_to,
 email_message_content_string=email_message_content_string,
 subject=EmailSubjectEnum.SUCCESS_LOGIN_SUBJECT
 )
```

4. Фоновая задача для отправки сообщения пользователю при успешном входе в приложение

Перед тем как приступать к написанию функции, которая будет отправлять сообщение пользователю, нам нужно создать зависимости для внедрения SMTP контроллера в эту фукнцию

1-й этап:

src/dependencies/repositories_factories.py

```
from aiosmtplib import SMTP

from settings import app_settings
from src.repositories import SMTPRepository
from src.repositories import StaticFilesRepository


def smtp_repository_factory(smtp_session: SMTP) -> SMTPRepository:
 """
 Фабрика репозиториев SMTP.

 :param smtp_session: Сессия SMTP.
 :return: Репозиторий SMTP.
 """

 return SMTPRepository(smtp_session=smtp_session, is_need_send_email=app_settings.IS_NEED_SEND_EMAIL)


def static_files_repository_factory(static_path: str = app_settings.STATIC_PATH) -> StaticFilesRepository:
 """
 Фабрика репозиториев для работы со статичными файлами.

 :return: Репозиторий для работы со статичными файлами.
 """

 return StaticFilesRepository(static_path=static_path)
```

2-й этап:

src/dependencies/controllers_factories.py

```
from src.controllers import SMTPController
from src.repositories import SMTPRepository
from src.repositories import StaticFilesRepository


def smtp_controller_factory(
 smtp_repository: SMTPRepository,
 static_files_repository: StaticFilesRepository
) -> SMTPController:
 """
 Фабрика контроллеров для работы с SMTP.

 :param smtp_repository: Репозиторий для работы с SMTP.
 :param static_files_repository: Репозиторий для работы со статическими файлами.
 :return: Контроллер для работы с SMTP.
 """

 return SMTPController(smtp_repository=smtp_repository, static_files_repository=static_files_repository)
```

3-й этап:

src/dependencies/common_factories.py

```
from typing import AsyncGenerator
from typing import Callable
from typing import Optional

from aiosmtplib import SMTP
from aiosmtplib import SMTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.builtin_types import CustomLogger


def get_sqlalchemy_async_session_generator(
 async_session_maker: async_sessionmaker[AsyncSession]
) -> Callable[[], AsyncGenerator[AsyncSession, None]]:
 async def sqlalchemy_async_session_generator() -> AsyncGenerator[AsyncSession, None]:
 """
 Генератор асинхронных сессий БД.

 :return: AsyncSession.
 """
 # TODO: Подумать над тем, чтобы перейти к контекстному менеджеру
 async_session = async_session_maker()
 try:
 yield async_session

 await async_session.commit()
 except SQLAlchemyError as exc:

 await async_session.rollback()
 await async_session.close()

 raise exc
 else:
 await async_session.close()

 return sqlalchemy_async_session_generator


def get_aiosmtplib_session_generator(
 hostname: str,
 port: int,
 username: str,
 password: str,
 timeout: int,
 use_tls: bool = False,
 start_tls: bool = False
) -> Callable[[], AsyncGenerator[Optional[SMTP], None]]:
 """
 Создание генератора асинхронной SMTP сессии.

 :param timeout: Таймаут подключения к SMTP (в секундах).
 :param hostname: Хост SMTP сервера.
 :param port: Порт SMTP сервера.
 :param username: Имя для подключения к SMTP.
 :param password: Пароль для подключения к SMTP.
 :param use_tls: Подключение к SMTP серверу через TLS/SSL. Если start_tls=True, поставить флаг False для use_tls.
 :param start_tls: Флаг для инициализации STARTTLS при подключении. Взаимоисключающее с use_tls.
 """

 async def aiosmtplib_session_generator() -> AsyncGenerator[Optional[SMTP], None]:
 """
 Генератор асинхронной сессии SMTP.

 :yield: Асинхронная сессия SMTP.
 """
 CustomLogger.info('Get aiosmtplib session')

 async_smtp_client = SMTP(
 hostname=hostname,
 port=port,
 username=username,
 password=password,
 use_tls=use_tls,
 start_tls=start_tls,
 timeout=timeout
 )

 try:
 await async_smtp_client.connect()
 CustomLogger.info(f'Success connection {async_smtp_client}')

 yield async_smtp_client
 except SMTPException as e:
 CustomLogger.error(f'Exception aiosmtplib session: {e}')

 async_smtp_client.close()

 yield None
 finally:
 CustomLogger.info('Close aiosmtplib session')

 if async_smtp_client.is_connected:
 await async_smtp_client.quit()

 return aiosmtplib_session_generator


def async_smtp_session_factory(
 hostname: str,
 port: int,
 username: str,
 password: str,
 timeout: int,
 use_tls: bool = False,
 start_tls: bool = False
) -> SMTP:
 """
 Фабрика для создания асинхронной сессии SMTP.

 :param timeout: Таймаут подключения к SMTP (в секундах).
 :param hostname: Хост SMTP сервера.
 :param port: Порт SMTP сервера.
 :param username: Имя для подключения к SMTP.
 :param password: Пароль для подключения к SMTP.
 :param use_tls: Подключение к SMTP серверу через TLS/SSL. Если start_tls=True, поставить флаг False для use_tls.
 :param start_tls: Флаг для инициализации STARTTLS при подключении. Взаимоисключающее с use_tls.
 :return: Асинхронная SMTP сессия.
 """
 CustomLogger.info('Get async smtp session')

 async_smtp_session = SMTP(
 hostname=hostname,
 port=port,
 username=username,
 password=password,
 timeout=timeout,
 use_tls=use_tls,
 start_tls=start_tls
 )

 return async_smtp_session
```

4-й этап:

src/dependencies/decorator_dependencies.py

```
from functools import wraps
from typing import Any
from typing import Callable
from typing import Coroutine

from aiosmtplib import SMTPException

from settings import app_settings
from src.builtin_types import CustomLogger
from .common_factories import async_smtp_session_factory
from .controllers_factories import smtp_controller_factory
from .repositories_factories import smtp_repository_factory
from .repositories_factories import static_files_repository_factory


def add_smtp_controller(
 func: Callable[..., Coroutine[Any, Any, None]]
) -> Callable[..., Coroutine[Any, Any, None]]:
 """
 Декоратор для добавления контроллера SMTP.
 Параметр в функции должен иметь имя 'smtp_controller'.

 :param func: Декорируемая функция.
 :return: Декорированная функция.
 """

 @wraps(func)
 async def wrapper(*args, **kwargs) -> None:
 async_smtp_session = async_smtp_session_factory(
 hostname=app_settings.SMTP_HOST,
 port=app_settings.SMTP_PORT,
 username=app_settings.SMTP_USER,
 password=app_settings.SMTP_PASSWORD,
 timeout=app_settings.SMTP_TIMEOUT,
 use_tls=app_settings.SMTP_USE_TLS,
 start_tls=app_settings.SMTP_START_TLS
 )

 smtp_controller = smtp_controller_factory(
 smtp_repository=smtp_repository_factory(smtp_session=async_smtp_session),
 static_files_repository=static_files_repository_factory()
 )

 try:
 await async_smtp_session.connect()

 await func(*args, **kwargs, smtp_controller=smtp_controller)
 except SMTPException as exc:
 CustomLogger.error(f'Exception smtp async session in {func.__name__}: {exc}')

 async_smtp_session.close()

 raise exc
 finally:
 CustomLogger.info(f'Close aiosmtplib session: {func.__name__}')

 if async_smtp_session.is_connected:
 await async_smtp_session.quit()

 return wrapper
```

5-й этап:

Создаём пакет background_tasks, где будут храниться все функции фоновых задач, в пакете src

В src/background_tasks создаём файл send_login_email_message_task.py:

```
from src.controllers import SMTPController
from src.dependencies import add_smtp_controller


@add_smtp_controller
async def send_login_email_message_task(
 email_to: str,
 username: str,
 smtp_controller: SMTPController
) -> None:
 """
 Фоновая задача отправки сообщения об успешном входе в приложения на почту пользователя.

 :param email_to: Почта адресата.
 :param username: Имя пользователя.
 :param smtp_controller: Контроллер для работы с SMTP.
 :return: None.
 """
 # Отправка сообщения на почту пользователя
 await smtp_controller.send_login_message(email_to=email_to, username=username)
```

5. Использование фоновой задачи в конечной точке для входа пользователя в приложение

```
from typing import Annotated

from fastapi import BackgroundTasks
from fastapi import Depends

from src.background_tasks import send_login_email_message_task
from src.controllers import AuthorizationController
from src.dependencies import get_authorization_controller
from src.schemas.requests import LoginRequestSchema
from src.schemas.responses import TokensResponse
from .custom_router import CustomRouter

web_authorization_router = CustomRouter(
 router_prefix='/authorization',
 name='Авторизация',
 description='Методы для работы с авторизацией',
 deprecated=False,
 dependencies=None,
 has_authentication=False
)


@web_authorization_router.api_router.post(path='/login')
async def user_login(
 login_request: LoginRequestSchema,
 authorization_controller: Annotated[AuthorizationController, Depends(get_authorization_controller)],
 background_tasks: BackgroundTasks
) -> TokensResponse:
 """
 Вход пользователя в приложение.
 """
 token_response, username, email = await authorization_controller.login_user(login_request=login_request)
 background_tasks.add_task(
 send_login_email_message_task,
 email_to=email,
 username=username
 )

 return token_response
```

Задача 1 – Самостоятельно переделать метод login_user(…) так, чтобы он возвращал не только токены, но и имя пользователя вместе с его e-mail

Вопрос 3 – Можно ли по другому внедрить SMTP контроллер в функцию отправки сообщения на почту, или единственный способ – использование декоратора?

Чтобы проверить работоспособность функции отправки сообщения на почту необходимо выполнить следующие шаги:

- Зайти в аккаунт Google

- Включить 2FA

- Добавить пароль приложений и сохранить выданный ключ

- Записать этот ключ в переменную SMTP_PASSWORD

- Изменить SMTP_HOST=smtp.gmail.com, SMTP_USER=ваш@gmail.com

ЗАДАНИЯ

- Создать ветку feature/lab6 от develop

- Создать репозиторий для работы с SMTP

- Создать контроллер для работы с SMTP

- Запустить контейнер с серверным приложением и проверить корректность отправки сообщения на почту

- Записать ответы на все вопросы в основной части в CHANGELOG.md

- Запушить ветку в удалённый репозиторий и создать Merge Request

ЛАБОРАТОРНАЯ РАБОТА 7

ФИНАЛЬНЫЙ ПРОЕКТ

Цель работы: Завершить разработку блога.

ВВЕДЕНИЕ

MyPy

MyPy — это статический анализатор типов для Python, который проверяет соответствие кода аннотациям типов без его выполнения. Он построен на основе системы типов PEP 484 и помогает выявлять ошибки, связанные с несоответствием типов, до запуска программы.

Ключевые особенности:

- Статическая проверка типов: MyPy анализирует аннотации типов (например, def func(x: int) -> str) и проверяет, что типы переменных, аргументов функций и возвращаемых значений используются согласованно.

- Интеграция с Python: Полностью поддерживает аннотации типов, введенные в Python 3.5+, и может проверять как типизированный, так и нетипизированный код.

- Гибкость: Позволяет постепенно внедрять типизацию — можно проверять только отдельные модули или использовать режим мягкой проверки.

- Поддержка сложных типов: Включает generics (обобщенные типы), union-типы (например, int | None), типы из модуля typing (например, List, Dict) и пользовательские типы.

- Конфигурация: Настройка через файл mypy.ini или pyproject.toml, где можно задавать правила проверки, игнорировать определенные ошибки или модули.

Применение:

- Обнаружение ошибок типизации: например, передача строки вместо числа.

- Улучшение читаемости и поддерживаемости кода за счет явных аннотаций.

- Интеграция в CI/CD-процессы для автоматической проверки типов.

Ограничения:

- Не проверяет логические ошибки или стиль кода.

- Требует явного указания типов для максимальной эффективности.

Flake8

Flake8 — это инструмент для проверки стиля кода и его соответствия стандартам PEP 8, а также обнаружения некоторых логических ошибок. Он объединяет несколько утилит: PyFlakes (анализ кода), pycodestyle (проверка стиля) и McCabe (оценка сложности кода).

Ключевые особенности:

- Проверка стиля (PEP 8): Flake8 проверяет отступы, длину строк, пробелы вокруг операторов, соглашения об именовании и другие стилистические нормы.

- Обнаружение ошибок: PyFlakes выявляет синтаксические ошибки, неиспользуемые переменные, импорты и другие потенциальные проблемы.

- Конфигурация: Настройка через файлы setup.cfg, tox.ini или .flake8, где можно игнорировать определенные правила, задавать максимальную длину строки или исключать файлы.

Применение:

- Обеспечение единого стиля кода в проекте.

- Раннее обнаружение потенциальных багов (например, неиспользуемых переменных).

- Улучшение читаемости и снижение сложности кода.

Ограничения:

- Не проверяет типы (в отличие от MyPy).

- Сфокусирован на стиле и базовых ошибках, а не на семантике программы.

Сравнение MyPy и Flake8

Назначение:

- MyPy проверяет типы и их корректное использование.

- Flake8 проверяет стиль и базовую корректность кода.

Тип анализа:

- MyPy выполняет статический анализ типов на основе аннотаций.

- Flake8 сочетает линтер (стиль и ошибки) и сложностной анализ.

Зависимость от аннотаций:

- MyPy требует аннотаций типов для глубокой проверки.

- Flake8 работает без аннотаций, анализируя сам код.

Интеграция:

- Оба инструмента часто используются вместе: Flake8 обеспечивает чистоту стиля, а MyPy — корректность типов.

- Могут настраиваться через общие файлы конфигурации (например, pyproject.toml).

ОСНОВНАЯ ЧАСТЬ

1. Добавление mypy и flake8 в проект

В корневой директории проекта создаём 2 файла: mypy.ini и tox.ini

mypy.ini

[mypy]
plugins = pydantic.mypy, sqlalchemy.ext.mypy.plugin
warn_return_any = True
warn_unused_configs = True
exclude = venv .venv
explicit_package_bases = True
follow_imports = silent
warn_redundant_casts = True
warn_unused_ignores = True
disallow_any_generics = True
check_untyped_defs = True
no_implicit_reexport = False

[pydantic-mypy]
init_forbid_extra = True
init_typed = True
warn_required_dynamic_aliases = True

[mypy-settings]
ignore_errors = True

tox.ini

```
[flake8]
max-line-length = 120
per-file-ignores =
 */__init__.py: F401
 */builtin_types/*: B039 F401
 */schemas/*: F401 A003 PYD002
 */dependencies/*: F401 B008
 */models/*: F821 A003
 */repositories/*: F401 E712
 */routers/*: B008
 mounted_application.py: B008
 settings.py: PYD002 PYD003
exclude =
 .git,
 requirements.txt,
 .venv,
 venv,
 .dockerignore,
 .env,
 .env.template,
 .gitignore,
 alembic.ini,
 CHANGELOG,
 docker-compose.yml,
 Dockerfile,
 entrypoint.sh,
 mypy.ini,
 README.md
 tox.ini
```

Обновить файл с зависимостями проекта:

```
fastapi==0.119.0
uvicorn==0.37.0
python-jose==3.3.0
passlib==1.7.4
bcrypt==4.3.0
aiosmtplib==5.0.0
aiofile==3.9.0
alembic==1.17.0
pydantic-settings==2.11.0
asyncpg==0.30.0
ping3==4.0.8
python-multipart==0.0.20
SQLAlchemy==2.0.43
aiohttp==3.13.2
flake8==6.0.0
flake8-bugbear==24.8.19
flake8-builtins==2.5.0
flake8-pydantic==0.3.1
mypy==1.7.1
types-flake8-bugbear==24.8.19.20240822
types-flake8-builtins==2.5.0.20240411
typing_extensions==4.14.1
types-passlib==1.7.7.20250408
types-python-jose==3.4.0.20250224
```

2. Применение mypy и flake8

Для запуска flake8 в терминале:

python -m flake8 . --config=tox.ini

Для запуска mypy в терминале:

python -m mypy . --config-file mypy.ini

Задание 1 – Решить все ошибки и предупреждения, которые подсветили flake8 и mypy

3. Обновление Dockerfile и docker-compose.yml

В корневой директории проекта создадим файл с точкой входа в приложение при запуске entrypoint.sh:

```
#!/bin/bash
alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000
```

В файле Dockerfile:

```
FROM python:3.12-slim
WORKDIR /app
COPY . /app

RUN apt-get update \
 && pip install --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements/requirements.txt \
 && pip cache purge \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
```

В файле docker-compose.yml:

```
services:
 blog-api:
 image: blog-api-image
 build:
 context: .
 dockerfile: Dockerfile
 container_name: blog-api
 ports:
 - "8000:8000"
 networks:
 - default
 environment:
 - APP=${APP}
 - HOST=${HOST}
 - PORT=${PORT}
 - SWAGGER_TITLE=${SWAGGER_TITLE}
 - APP_VERSION=${APP_VERSION}
 - ROOT_PATH=${ROOT_PATH}
 - IS_DEBUG=${IS_DEBUG}
 - STATIC_PATH=${STATIC_PATH}
 - AUTH_URL=${SERVER_AUTH_URL}
 - USERS_SQL_SCHEMA=${USERS_SQL_SCHEMA}
 - POSTS_SQL_SCHEMA=${POSTS_SQL_SCHEMA}
 - SQL_DSN=${SERVER_SQL_DSN}
 - SMTP_HOST=${SMTP_HOST}
 - SMTP_PORT=${SMTP_PORT}
 - SMTP_USER=${SMTP_USER}
 - SMTP_PASSWORD=${SMTP_PASSWORD}
 - SMTP_TIMEOUT=${SMTP_TIMEOUT}
 - SMTP_USE_TLS=${SMTP_USE_TLS}
 - SMTP_START_TLS=${SMTP_START_TLS}
 - SMTP_ALLOWED_SENDER_DOMAINS=${SMTP_ALLOWED_SENDER_DOMAINS}
 database:
 image: postgres:17
 container_name: database
 environment:
 - POSTGRES_USER=${POSTGRES_USER}
 - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
 - POSTGRES_HOST=${POSTGRES_HOST}
 - POSTGRES_DB=${POSTGRES_DB}
 ports:
 - 5432:5432
 networks:
 - default
 restart: always
 volumes:
 - postgres_data:/var/lib/postgresql/data

networks:
 default:
 driver: bridge

volumes:
 postgres_data:
```

ЗАДАНИЯ

- Создать ветку feature/lab7 от develop

- Прогнать flake8 и mypy для всего проекта и решить все предупреждения и ошибки

- Добавить поле `user_id` к PostModel и PostFullDto

- При создании постов присваивать ID пользователя, который этот пост создал

- Сделать конечную точку для отбора постов по ID пользователя и с фильтрами пагинации и датой создания

- Нарисовать ERD-схему и включить изображени и файл erd_schema.drawio в проект

- Запустить Docker контейнер и проверить работоспособность всего приложения

- Записать ответы на все вопросы в основной части в CHANGELOG.md

- Запушить ветку в удалённый репозиторий и создать Merge Request
