from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Groups, Themes
from database.queries import QueryBase


class QuerySelectGroupByTheme(QueryBase):
    """
    Describes the request for selecting groups by theme.
    """
    @staticmethod
    async def query(session: AsyncSession, theme: Themes.theme):
        res = await session.execute(
            select(
                Groups.group_name,
                Themes.theme,
                Groups.link
            ).join(Themes,
                   Themes.id == Groups.theme_id,
                   isouter=False
                   ).where(Themes.theme == theme)
        )
        return (item for item in res.all())
