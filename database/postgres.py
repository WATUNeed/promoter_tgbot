import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

from database.dsm_base import DSMBase
from database.queries import QueryBase
from data.settings import settings


class Postgres(DSMBase):
    """
    Describes the Postgres database object.
    :param engine:
    """
    __slots__ = ('engine', )

    def __init__(self):
        self.engine = create_async_engine(settings.databases.postgresql_url, future=True)

    @asynccontextmanager
    async def get_session(self):
        """
        Creates an asynchronous context manager for a session with Postgres.
        If an error occurs during the query process, it rolls back the database.
        Closes database connection after query completes.
        :return:
        """
        try:
            async_session = sessionmaker(self.engine, class_=AsyncSession)

            async with async_session() as session:
                yield session
        except Exception as e:
            await session.rollback()
            logging.exception(f'Exception when executing an SQL query: {e}')
        finally:
            await session.close()

    async def make_request(self, query_class: QueryBase, *args, **kwargs):
        """
        Opens asynchronous connection to Postgres and executes query.
        :param query_class: class to call the query. Any class that inherits the QueryBase.
        :param args: parameters for the query function.
        :param kwargs:
        :return: query result or None.
        """
        async with self.get_session() as session:
            response = await query_class.query(session, *args, **kwargs)
            await session.commit()
            if response:
                return response
