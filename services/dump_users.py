from datetime import datetime

from data.settings import settings
from database.models import Users
from database.queries.select_all_users import QuerySelectAllUsers
from loader import db
from utils import write_xlsx


async def create_dump_users() -> str:
    """
    Queries the database for a list of users and creates a dump file.
    :return: users dump file and filename
    """
    scheme = (Users.id, Users.user_id, Users.full_name, Users.is_admin)

    users = await db.make_request(QuerySelectAllUsers)

    filename = ''.join(
        [settings.paths.dumps[-2]] +
        [f'{datetime.now().strftime("%m_%d_%Y")}'] +
        [settings.paths.dumps[-1]]
    )

    path = settings.paths.dumps[:-2] + [filename]

    await write_xlsx('\\'.join(path), [scheme] + users)

    return filename
