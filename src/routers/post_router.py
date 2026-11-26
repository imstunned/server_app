"""Роутер для работы с постами."""

from typing import Annotated
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import status

from src.controllers import PostController
from src.dependencies import get_post_controller
from src.schemas.data_transfer_objects import PostCreateDto
from src.schemas.data_transfer_objects import PostFullDto
from src.schemas.data_transfer_objects import PostShortDto
from src.schemas.data_transfer_objects import PostUpdateDto

post_router = APIRouter(
    prefix='/post',
    tags=['Посты'],
    deprecated=False,
    dependencies=None,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': 'Пост не найден',
        },
    },
)


@post_router.get(
    path='/many',
    summary='Список постов',
    description='Возвращает список всех постов блога.',
    response_description='Список кратких DTO постов.',
)
async def get_post_many(
    post_controller: Annotated[PostController, Depends(get_post_controller)],
) -> List[PostShortDto]:
    """
    Получение списка постов.
    """

    return await post_controller.get_post_many()


@post_router.get(
    path='/{post_id}',
    summary='Пост по ID',
    description='Возвращает один пост по его идентификатору.',
    response_description='Полный DTO поста.',
)
async def get_post_by_id(
    post_controller: Annotated[PostController, Depends(get_post_controller)],
    post_id: int = Path(
        description='ID поста',
        ge=1,
        examples=[1],
    ),
) -> PostFullDto:
    """
    Получение информации о посте.
    """

    post = await post_controller.get_post_by_id(post_id=post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пост не найден',
        )

    return post


@post_router.post(
    path='',
    status_code=status.HTTP_201_CREATED,
    summary='Создание поста',
    description='Создаёт новый пост блога.',
    response_description='Полный DTO созданного поста.',
)
async def create_post(
    post_create_dto: PostCreateDto,
    post_controller: Annotated[PostController, Depends(get_post_controller)],
) -> PostFullDto:
    """
    Создание поста.
    """

    return await post_controller.create_post(post_create_dto=post_create_dto)


@post_router.patch(
    path='/{post_id}',
    summary='Обновление поста',
    description='Частично обновляет поля поста.',
    response_description='Полный DTO обновлённого поста.',
)
async def update_post(
    post_update_dto: PostUpdateDto,
    post_controller: Annotated[PostController, Depends(get_post_controller)],
    post_id: int = Path(
        description='ID поста',
        ge=1,
        examples=[1],
    ),
) -> PostFullDto:
    """
    Обновление поста.
    """

    post = await post_controller.update_post(post_id=post_id, post_update_dto=post_update_dto)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пост не найден',
        )

    return post


@post_router.delete(
    path='/{post_id}',
    summary='Удаление поста',
    description='Удаляет пост по его идентификатору.',
    response_description='Признак успешного удаления.',
)
async def delete_post(
    post_controller: Annotated[PostController, Depends(get_post_controller)],
    post_id: int = Path(
        description='ID поста',
        ge=1,
        examples=[1],
    ),
) -> bool:
    """
    Удаление поста.
    """

    is_deleted = await post_controller.delete_post(post_id=post_id)

    if not is_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пост не найден',
        )

    return is_deleted
