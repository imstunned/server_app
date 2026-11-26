"""Роутер для работы с пользователями."""

from typing import Annotated
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import status

from src.controllers import UserController
from src.dependencies import get_user_controller
from src.schemas.data_transfer_objects import UserCreateDto
from src.schemas.data_transfer_objects import UserShortDto
from src.schemas.data_transfer_objects import UserUpdateDto

user_router = APIRouter(
    prefix='/user',
    tags=['Пользователи'],
    deprecated=False,
    dependencies=None,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'description': 'Пользователь не найден',
        },
    },
)


@user_router.get(
    path='/many',
    summary='Список пользователей',
    description='Возвращает список всех пользователей.',
    response_description='Список кратких DTO пользователей.',
)
async def get_user_many(
    user_controller: Annotated[UserController, Depends(get_user_controller)],
) -> List[UserShortDto]:
    """
    Получение списка пользователей.
    """

    return await user_controller.get_user_many()


@user_router.get(
    path='/{user_id}',
    summary='Пользователь по ID',
    description='Возвращает одного пользователя по его идентификатору.',
    response_description='Краткий DTO пользователя.',
)
async def get_user_by_id(
    user_controller: Annotated[UserController, Depends(get_user_controller)],
    user_id: int = Path(
        description='ID пользователя',
        ge=1,
        examples=[1],
    ),
) -> UserShortDto:
    """
    Получение информации о пользователе.
    """

    user = await user_controller.get_user_by_id(user_id=user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден',
        )

    return user


@user_router.post(
    path='',
    status_code=status.HTTP_201_CREATED,
    summary='Создание пользователя',
    description='Создаёт нового пользователя (пароль хэшируется).',
    response_description='Краткий DTO созданного пользователя.',
)
async def create_user(
    user_create_dto: UserCreateDto,
    user_controller: Annotated[UserController, Depends(get_user_controller)],
) -> UserShortDto:
    """
    Создание пользователя.
    """

    return await user_controller.create_user(user_create_dto=user_create_dto)


@user_router.patch(
    path='/{user_id}',
    summary='Обновление пользователя',
    description='Частично обновляет поля пользователя.',
    response_description='Краткий DTO обновлённого пользователя.',
)
async def update_user(
    user_update_dto: UserUpdateDto,
    user_controller: Annotated[UserController, Depends(get_user_controller)],
    user_id: int = Path(
        description='ID пользователя',
        ge=1,
        examples=[1],
    ),
) -> UserShortDto:
    """
    Обновление пользователя.
    """

    user = await user_controller.update_user(user_id=user_id, user_update_dto=user_update_dto)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден',
        )

    return user


@user_router.delete(
    path='/{user_id}',
    summary='Удаление пользователя',
    description='Удаляет пользователя по его идентификатору.',
    response_description='Признак успешного удаления.',
)
async def delete_user(
    user_controller: Annotated[UserController, Depends(get_user_controller)],
    user_id: int = Path(
        description='ID пользователя',
        ge=1,
        examples=[1],
    ),
) -> bool:
    """
    Удаление пользователя.
    """

    is_deleted = await user_controller.delete_user(user_id=user_id)

    if not is_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден',
        )

    return is_deleted
