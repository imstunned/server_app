"""Базовый репозиторий для работы с БД."""

from typing import Generic
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

from sqlalchemy import delete
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.exceptions import ConflictError
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
        short_schema_type: Type[ShortSchema],
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

        if model:
            return self._full_schema_type.model_validate(obj=model)

        return None

    async def get_many_full(self) -> List[FullSchema]:
        """
        Получение списка полных DTO.

        :return: Список полных DTO.
        """

        statement = select(self._model_type)
        result = await self._async_db_session.execute(statement)

        return [
            self._full_schema_type.model_validate(obj=model)
            for model in result.scalars().all()
        ]

    async def get_many_short(self) -> List[ShortSchema]:
        """
        Получение списка кратких DTO.

        :return: Список кратких DTO.
        """

        statement = select(self._model_type)
        result = await self._async_db_session.execute(statement)

        return [
            self._short_schema_type.model_validate(obj=model)
            for model in result.scalars().all()
        ]

    async def upsert(self, dto: FullSchema) -> FullSchema:
        """
        Создание или обновление одного объекта в БД.

        :param dto: Полный DTO объекта.
        :return: Полный DTO объекта.
        """

        values = dto.model_dump(exclude={'id'}, exclude_none=True)

        if dto.id is None:
            model = self._model_type(**values)
            self._async_db_session.add(model)
        else:
            model = await self._async_db_session.get(self._model_type, dto.id)

            if model is None:
                raise ValueError(f'{self._model_type.__name__} with id={dto.id} not found')

            for field_name, value in values.items():
                setattr(model, field_name, value)

        try:
            await self._async_db_session.flush()
            await self._async_db_session.refresh(model)
            # Коммитим до возврата ответа клиенту: иначе следующий запрос может
            # прийти раньше коммита (teardown зависимости выполняется после отправки
            # ответа) и увидеть устаревшие данные.
            await self.commit()
        except IntegrityError as exc:
            await self._async_db_session.rollback()

            raise ConflictError('Нарушено ограничение уникальности данных') from exc

        return self._full_schema_type.model_validate(obj=model)

    async def delete_one_by_id(self, object_id: int) -> bool:
        """
        Удаление одного объекта по ID.

        :param object_id: ID объекта.
        :return: Признак успешного удаления.
        """

        delete_statement = delete(
            self._model_type,
        ).where(
            self._model_type.id == object_id,
        )

        result = await self._async_db_session.execute(statement=delete_statement)
        await self.commit()

        return result.rowcount == 1
