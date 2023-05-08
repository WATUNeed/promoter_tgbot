"""
To create a new query:
1) Create module database.queries.<query_name>.py
2) Create class <QueryName> and inherit from QueryBase class
3) Implement query method
4) Add to database.queries.__init__.py: "from .<query_name> import <QueryName>"
"""
import abc


class QueryBase(metaclass=abc.ABCMeta):
    """
    Template for creating query objects.
    """
    @staticmethod
    @abc.abstractmethod
    async def query(*args, **kwargs):
        pass
