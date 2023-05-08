import os
from os import getenv
from dataclasses import dataclass


@dataclass(slots=True, repr=True, init=True)
class Bots:
    bot_token: str
    admins: tuple
    themes: tuple
    message_delay: int | float


@dataclass(slots=True, repr=True, init=True)
class Databases:
    postgresql_url: str


@dataclass(slots=True, repr=True, init=True)
class Paths:
    dumps: list


@dataclass(slots=True, repr=True, init=True)
class Settings:
    bots: Bots
    databases: Databases
    paths: Paths


def __get_settings() -> Settings:
    if getenv('ADMINS'):
        admins = tuple(
            filter(None, map(lambda admin: int(admin) if len(admin) > 1 else None, getenv('ADMINS').split(',')))
        )
    else:
        admins = ()

    return Settings(
        bots=Bots(
            bot_token=getenv('BOT_TOKEN'),
            admins=admins,
            themes=(),
            message_delay=0.5
        ),
        databases=Databases(
            postgresql_url=getenv('POSTGRESQL_URL')
        ),
        paths=Paths(
            dumps=os.getcwd().split('\\') + ['dumps'] + ['users_dump_'] + ['.xlsx']
        )
    )


settings: Settings = __get_settings()
