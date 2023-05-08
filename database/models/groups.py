from sqlalchemy import (
    Column,
    Integer,
    String,
    Identity,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database.models.model_base import ModelBase


class Groups(ModelBase):
    """
    Describes the entity model of the groups.
    :param id:
    :param group_name:
    :param link:
    :param theme_id:
    :param themes_rel:
    """
    __tablename__ = 'groups'

    id = Column(Integer, Identity(increment=1, start=1, minvalue=1, maxvalue=2147483647), primary_key=True, unique=True)
    group_name = Column(String(255), nullable=False)
    link = Column(String, nullable=False)
    theme_id = Column(Integer, ForeignKey('themes.id'))

    themes_rel = relationship("Themes")

    def __init__(self, id: int, group_name: str, link: str, theme_id: int):
        self.id = id
        self.group_name = group_name
        self.link = link
        self.theme_id = theme_id

    def __repr__(self):
        return f'id: {self.id} name: {self.group_name} link: {self.link} theme_id: {self.theme_id}'
