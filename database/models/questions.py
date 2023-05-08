from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Identity
)
from sqlalchemy.orm import relationship

from database.models.model_base import ModelBase


class Questions(ModelBase):
    """
    Describes the entity model of the questions.
    :param id:
    :param question:
    :param theme_id:
    :param themes_rel:
    """
    __tablename__ = 'questions'

    id = Column(Integer, Identity(increment=1, start=1, minvalue=1, maxvalue=2147483647), primary_key=True, unique=True)
    question = Column(String, unique=True, nullable=False)
    theme_id = Column(Integer, ForeignKey('themes.id'))

    themes_rel = relationship("Themes")

    def __init__(self, id: int, question: str, theme_id: int):
        self.id = id
        self.question = question
        self.theme_id = theme_id

    def __repr__(self):
        return f'id: {self.id} question: {self.question} theme_id: {self.theme_id}'
