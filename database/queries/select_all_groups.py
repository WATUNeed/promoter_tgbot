from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Groups, Themes
from database.queries import QueryBase


class QuerySelectAllGroups(QueryBase):
    """
    Describes the request to select all groups.
    """
    @staticmethod
    async def query(session: AsyncSession):
        res = await session.execute(
            select(
                Groups.group_name,
                Themes.theme,
                Groups.link
            ).join(Themes,
                   Themes.id == Groups.theme_id,
                   isouter=False
                   ))
        return (item for item in res.all())
