from dataclasses import dataclass

from database.queries import QuerySelectQuestionByTheme
from loader import db


@dataclass(slots=True, repr=True, init=True)
class Question:
    question: str


async def get_questions_by_theme(theme: str) -> list[Question]:
    """
    :return: Returns all groups.
    """
    questions = await db.make_request(QuerySelectQuestionByTheme, theme)
    return [Question(question) for question in questions][::-1]
