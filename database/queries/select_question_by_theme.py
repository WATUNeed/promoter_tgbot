from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Themes, Questions
from database.queries import QueryBase


class QuerySelectQuestionByTheme(QueryBase):
    """
    Describes a request for a selection of questions on a theme.
    """
    @staticmethod
    async def query(session: AsyncSession, theme: Themes.theme):
        res = await session.execute(
            select(
                Questions.question
            ).join(Themes,
                   Themes.id == Questions.theme_id,
                   isouter=False
                   ).where(Themes.theme == theme)
        )
        return [item[0] for item in res.all()]
