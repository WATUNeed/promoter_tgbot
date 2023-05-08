from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from database.postgres import Postgres

from data.settings import settings


db = Postgres()

storage = MemoryStorage()

bot = Bot(token=settings.bots.bot_token, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot, storage=storage)
