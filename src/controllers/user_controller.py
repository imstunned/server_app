"""Контроллер для работы с пользователями."""

from typing import List
from typing import Optional

from passlib.context import CryptContext

from src.exceptions import ConflictError
from src.interfaces.controllers import BaseControllerInterface
from src.repositories import UserRepository
from src.schemas.data_transfer_objects import UserCreateDto
from src.schemas.data_transfer_objects import UserFullDto
from src.schemas.data_transfer_objects import UserShortDto
from src.schemas.data_transfer_objects import UserUpdateDto
from src.utils import CommonUtils


class UserController(BaseControllerInterface):
    """
    Контроллер для работы с пользователями.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        password_context: CryptContext,
    ):
        self._user_repository = user_repository
        self._password_context = password_context

    async def get_user_by_id(self, user_id: int) -> Optional[UserShortDto]:
        """
        Получение пользователя по ID.

        :param user_id: ID пользователя.
        :return: Краткий DTO пользователя.
        """

        user_full_dto = await self._user_repository.get_one_full_by_id(object_id=user_id)

        if user_full_dto is None:
            return None

        return UserShortDto.model_validate(obj=user_full_dto)

    async def get_user_many(self) -> List[UserShortDto]:
        """
        Получение списка пользователей.

        :return: Список кратких DTO пользователей.
        """

        return await self._user_repository.get_many_short()

    async def create_user(self, user_create_dto: UserCreateDto) -> UserShortDto:
        """
        Создание пользователя.

        :param user_create_dto: DTO нового пользователя.
        :return: Краткий DTO созданного пользователя.
        :raise ConflictError: Если пользователь с таким логином уже существует.
        """

        existing_user = await self._user_repository.get_user_by_login(login=user_create_dto.login)

        if existing_user is not None:
            raise ConflictError('Пользователь с таким логином уже существует')

        user_full_dto = UserFullDto(
            username=user_create_dto.username,
            email=user_create_dto.email,
            login=user_create_dto.login,
            password=CommonUtils.get_password_hash(
                plain_password=user_create_dto.password,
                password_context=self._password_context,
            ),
        )
        created_user = await self._user_repository.upsert(dto=user_full_dto)

        return UserShortDto.model_validate(obj=created_user)

    async def update_user(self, user_id: int, user_update_dto: UserUpdateDto) -> Optional[UserShortDto]:
        """
        Обновление пользователя.

        :param user_id: ID пользователя.
        :param user_update_dto: DTO с изменяемыми полями.
        :return: Краткий DTO обновлённого пользователя.
        """

        user_full_dto = await self._user_repository.get_one_full_by_id(object_id=user_id)

        if user_full_dto is None:
            return None

        update_values = user_update_dto.model_dump(exclude_none=True)

        if 'password' in update_values:
            update_values['password'] = CommonUtils.get_password_hash(
                plain_password=update_values['password'],
                password_context=self._password_context,
            )

        user_full_dto = user_full_dto.model_copy(update=update_values)
        updated_user = await self._user_repository.upsert(dto=user_full_dto)

        return UserShortDto.model_validate(obj=updated_user)

    async def delete_user(self, user_id: int) -> bool:
        """
        Удаление пользователя.

        :param user_id: ID пользователя.
        :return: Признак успешного удаления.
        """

        return await self._user_repository.delete_one_by_id(object_id=user_id)
