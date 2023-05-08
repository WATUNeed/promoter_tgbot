from typing import Collection

import aiofiles
from aiocsv import AsyncWriter


async def write_xlsx(path: str, data: Collection):
    """
    Asynchronous data recording to xlsx file.
    :param path: path to xlsx file
    :param data: List of data to be entered. The first item in the list will be used to name the columns.
    :return:
    """
    async with aiofiles.open(path, mode='w') as f:
        writer = AsyncWriter(f, lineterminator='\r')
        await writer.writerows(data)
