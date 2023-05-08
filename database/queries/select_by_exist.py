from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.queries import QueryBase


class QuerySelectByExist(QueryBase):
    """
    Describes a request to check for the existence of a tuple.
    """
    @staticmethod
    async def query(session: AsyncSession, table, attribute, condition):
        res = await session.execute(
            select(
                table
            ).where(attribute == condition)
        )
        return res.fetchone()

