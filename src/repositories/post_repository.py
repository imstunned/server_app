"""Репозиторий для работы с постами (хранение в памяти)."""

from typing import List
from typing import Optional

from src.interfaces.repositories import BaseRepositoryInterface
from src.schemas.data_transfer_objects import PostFullDto
from src.schemas.data_transfer_objects import PostUpdateDto


class PostRepository(BaseRepositoryInterface):
    """
    Репозиторий для работы с постами.
    """

    def __init__(self, posts: List[PostFullDto]):  # TODO: Заглушка, позже перейти на сессии БД
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

    async def create_post(self, post: PostFullDto) -> PostFullDto:
        """
        Создание поста.

        :param post: DTO нового поста.
        :return: Полный DTO созданного поста.
        """

        new_id = max((existing_post.id or 0 for existing_post in self._posts), default=0) + 1
        created_post = post.model_copy(update={'id': new_id})
        self._posts.append(created_post)

        return created_post

    async def update_post(self, post_id: int, post_update: PostUpdateDto) -> Optional[PostFullDto]:
        """
        Обновление поста по его ID.

        :param post_id: ID поста.
        :param post_update: DTO с изменяемыми полями.
        :return: Полный DTO обновлённого поста.
        """

        for index, post in enumerate(self._posts):
            if post.id == post_id:
                updated_post = post.model_copy(
                    update=post_update.model_dump(exclude_none=True),
                )
                self._posts[index] = updated_post

                return updated_post

        return None

    async def delete_post(self, post_id: int) -> bool:
        """
        Удаление поста по его ID.

        :param post_id: ID поста.
        :return: Признак успешного удаления.
        """

        for index, post in enumerate(self._posts):
            if post.id == post_id:
                self._posts.pop(index)

                return True

        return False
