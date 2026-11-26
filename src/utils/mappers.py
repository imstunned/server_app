"""Мапперы (сборка DTO)."""

from src.schemas.data_transfer_objects import PostCreateDto
from src.schemas.data_transfer_objects import PostFullDto


class PostFullDtoMapper:
    """
    Сборка полного DTO поста.
    """

    @staticmethod
    def map_from_create_dto(post_create_dto: PostCreateDto) -> PostFullDto:
        """
        Сборка полного DTO поста из DTO создания.

        :param post_create_dto: DTO создания поста.
        :return: Полный DTO поста.
        """

        return PostFullDto(
            author_id=post_create_dto.author_id,
            name=post_create_dto.name,
            content=post_create_dto.content,
        )
