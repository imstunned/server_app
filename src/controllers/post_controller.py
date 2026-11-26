"""Контроллер для работы с постами."""

from typing import List
from typing import Optional

from src.interfaces.controllers import BaseControllerInterface
from src.repositories import PostRepository
from src.schemas.data_transfer_objects import PostCreateDto
from src.schemas.data_transfer_objects import PostFullDto
from src.schemas.data_transfer_objects import PostShortDto
from src.schemas.data_transfer_objects import PostUpdateDto
from src.utils import PostFullDtoMapper


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

        return await self._post_repository.get_one_full_by_id(object_id=post_id)

    async def get_post_many(self) -> List[PostShortDto]:
        """
        Получение списка постов.

        :return: Список кратких DTO постов.
        """

        return await self._post_repository.get_many_short()

    async def create_post(self, post_create_dto: PostCreateDto) -> PostFullDto:
        """
        Создание поста.

        :param post_create_dto: DTO нового поста.
        :return: Полный DTO созданного поста.
        """

        post_full_dto = PostFullDtoMapper.map_from_create_dto(post_create_dto=post_create_dto)

        return await self._post_repository.upsert(dto=post_full_dto)

    async def update_post(self, post_id: int, post_update_dto: PostUpdateDto) -> Optional[PostFullDto]:
        """
        Обновление поста.

        :param post_id: ID поста.
        :param post_update_dto: DTO с изменяемыми полями.
        :return: Полный DTO обновлённого поста.
        """

        post_full_dto = await self._post_repository.get_one_full_by_id(object_id=post_id)

        if post_full_dto is None:
            return None

        post_full_dto = post_full_dto.model_copy(
            update=post_update_dto.model_dump(exclude_none=True),
        )

        return await self._post_repository.upsert(dto=post_full_dto)

    async def delete_post(self, post_id: int) -> bool:
        """
        Удаление поста.

        :param post_id: ID поста.
        :return: Признак успешного удаления.
        """

        return await self._post_repository.delete_one_by_id(object_id=post_id)
