from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

from data.settings import settings


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: Message):
        return message.from_user.id in settings.bots.admins
