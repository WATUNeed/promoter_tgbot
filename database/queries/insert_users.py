from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Users
from database.models.model_base import ModelBase
from database.queries import QueryBase


class QueryInsertUsers(QueryBase):
    """
    Describes a request to enter a user.
    """
    @staticmethod
    async def query(
            session: AsyncSession,
            table: ModelBase,
            user_id: Users.user_id,
            full_name: Users.full_name,
            is_admin: Users.is_admin
    ):
        await session.execute(
            insert(Users).values(
                user_id=user_id,
                full_name=full_name,
                is_admin=is_admin
            )
        )
