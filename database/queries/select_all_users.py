from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Users
from database.queries import QueryBase


class QuerySelectAllUsers(QueryBase):
    """
    Describes a request to select all users.
    """
    @staticmethod
    async def query(session: AsyncSession):
        scheme = (Users.id, Users.user_id, Users.full_name, Users.is_admin)
        res = await session.execute(
            select(*scheme)
        )
        return [item for item in res.all()]
