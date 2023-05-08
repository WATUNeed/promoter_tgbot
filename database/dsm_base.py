import abc

from database.queries import QueryBase


class DSMBase(metaclass=abc.ABCMeta):
    """
    Template for connecting a relational database management system.
    """
    @abc.abstractmethod
    async def make_request(self, query_class: QueryBase, *args, **kwargs):
        pass
