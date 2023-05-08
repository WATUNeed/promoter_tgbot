from dataclasses import dataclass
from typing import Generator

from database.queries import QuerySelectAllGroups, QuerySelectGroupByTheme
from loader import db


@dataclass(slots=True, repr=True, init=True)
class Group:
    name: str
    theme: str
    link: str


async def _tuple_to_group_generator(groups: Generator[tuple, None, None]) -> Generator[Group, None, None]:
    """
    Converts the tuple generator into a Group generator
    :param groups:  of groups
    :return:
    """
    return (Group(group[0], group[1], group[2]) for group in groups)


async def get_groups() -> Generator[Group, None, None]:
    """
    :return: Returns all groups.
    """
    groups = await db.make_request(QuerySelectAllGroups)
    return await _tuple_to_group_generator(groups)


async def get_groups_by_theme(theme: str) -> Generator[Group, None, None]:
    """
    :return: Returns all groups by theme.
    """
    groups = await db.make_request(QuerySelectGroupByTheme, theme)
    return await _tuple_to_group_generator(groups)
