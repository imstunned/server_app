"""Контроллер для работы с постами."""

from typing import List
from typing import Optional

from src.interfaces.controllers import BaseControllerInterface
from src.repositories import PostRepository
from src.schemas.data_transfer_objects import PostFullDto
from src.schemas.data_transfer_objects import PostUpdateDto


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

    async def create_post(self, post: PostFullDto) -> PostFullDto:
        """
        Создание поста.

        :param post: DTO нового поста.
        :return: Полный DTO созданного поста.
        """

        return await self._post_repository.create_post(post=post)

    async def update_post(self, post_id: int, post_update: PostUpdateDto) -> Optional[PostFullDto]:
        """
        Обновление поста.

        :param post_id: ID поста.
        :param post_update: DTO с изменяемыми полями.
        :return: Полный DTO обновлённого поста.
        """

        return await self._post_repository.update_post(post_id=post_id, post_update=post_update)

    async def delete_post(self, post_id: int) -> bool:
        """
        Удаление поста.

        :param post_id: ID поста.
        :return: Признак успешного удаления.
        """

        return await self._post_repository.delete_post(post_id=post_id)
