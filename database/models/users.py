from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Identity
)

from database.models.model_base import ModelBase


class Users(ModelBase):
    """
    Describes the entity model of the users.
    :param id:
    :param user_id:
    :param full_name:
    :param is_admin:
    """
    __tablename__ = 'users'

    id = Column(Integer, Identity(increment=1, start=1, minvalue=1, maxvalue=2147483647), primary_key=True, unique=True)
    user_id = Column(String, unique=True, nullable=False)
    full_name = Column(String(50))
    is_admin = Column(Boolean, nullable=False)

    def __init__(self, id: int, user_id: int, full_name: str, is_admin: bool):
        self.id = id
        self.user_id = user_id
        self.full_name = full_name
        self.is_admin = is_admin

    def __repr__(self):
        return f'id: {self.id} user_id: {self.user_id} full_name: {self.full_name} is_amin: {self.is_admin}'
