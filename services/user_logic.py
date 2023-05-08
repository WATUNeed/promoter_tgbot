import logging
from dataclasses import dataclass
from typing import Generator

from database.models import Users
from database.queries import QuerySelectByExist, QueryInsertUsers, QuerySelectAttributes
from loader import db


@dataclass(slots=True, repr=True, init=True)
class User:
    user_id: int


async def create_user(user_id: str, full_name: str, is_admin: bool):
    """
    Checks if the user exists in the database. If not, creates it.
    :param is_admin:
    :param full_name:
    :param user_id:
    :return:
    """
    if not await user_exists(user_id):
        await db.make_request(
            QueryInsertUsers,
            table=Users,
            user_id=user_id,
            full_name=full_name,
            is_admin=is_admin
        )


async def get_users() -> Generator[User, None, None]:
    """
    :return: Returns all user_id from the database.
    """
    response = await db.make_request(QuerySelectAttributes, Users.user_id)
    return (User(user_id=user) for user in response)


async def user_exists(user_id: str) -> bool:
    """
    Checks if the user exists in the database.
    :param user_id:
    :return:
    """
    if not isinstance(user_id, str):
        logging.exception(f'TypeError type of "user_id" should be str.')
        raise TypeError(f'TypeError type of "user_id" should be str.')

    return await db.make_request(QuerySelectByExist, Users, Users.user_id, user_id)
