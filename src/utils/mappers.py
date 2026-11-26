"""Мапперы (сборка DTO)."""

from src.schemas.data_transfer_objects import PostFullDto


class PostFullDtoMapper:
    """
    Сборка полного DTO поста.
    """

    @staticmethod
    def map_post_full_dto(
        post_id: int,
        author_name: str,
        content: str,
    ) -> PostFullDto:
        """
        Сборка полного DTO поста.

        :param post_id: ID поста.
        :param author_name: Имя автора.
        :param content: Содержание поста.
        :return: Полный DTO поста.
        """

        return PostFullDto(
            id=post_id,
            author_name=author_name,
            content=content,
        )
