from sqlalchemy import (
    Column,
    Integer,
    String,
    Identity
)

from sqlalchemy.orm import relationship

from database.models.model_base import ModelBase


class Themes(ModelBase):
    """
    Describes the entity model of the themes.
    :param id:
    :param theme:
    :param groups_rel:
    :param questions_rel:
    """
    __tablename__ = 'themes'

    id = Column(Integer, Identity(increment=1, start=1, minvalue=1, maxvalue=2147483647), primary_key=True, unique=True)
    theme = Column(String(255), nullable=False)

    groups_rel = relationship("Groups")
    questions_rel = relationship("Questions")

    def __init__(self, id: int, theme: str, polling_question: str):
        self.id = id
        self.theme = theme
        self.polling_question = polling_question

    def __repr__(self):
        return f'id: {self.id} theme: {self.theme} polling_question: {self.polling_question}'
