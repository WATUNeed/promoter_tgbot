from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.queries import QueryBase


class QuerySelectAttributes(QueryBase):
    """
    Describes a request to select attributes of an entity.
    """
    @staticmethod
    async def query(session: AsyncSession, *args, **kwargs):
        attributes = tuple(filter(None, (*args, *kwargs.values())))
        res = await session.execute(
            select(*attributes)
        )
        return [item[0] if len(attributes) == 1 else tuple(filter(None, item)) for item in res.all()]
