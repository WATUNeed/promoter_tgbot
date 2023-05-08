import logging

from aiogram import executor, Dispatcher
from aiogram.utils.exceptions import ChatNotFound

from database.models import Themes
from database.queries import QuerySelectAttributes
from loader import dp, db, bot
from data.settings import settings
from utils import async_generator


async def on_startup(dp_: Dispatcher):
    import handlers
    import filters

    async for admin in async_generator(settings.bots.admins, settings.bots.message_delay):
        try:
            await bot.send_message(chat_id=admin, text='Бот запущен')
        except ChatNotFound as e:
            logging.exception(f'Admin chat was not found: {e}')

    settings.bots.themes = await db.make_request(QuerySelectAttributes, Themes.theme)


async def on_shutdown(dp_: Dispatcher):
    async for admin in async_generator(settings.bots.admins, settings.bots.message_delay):
        try:
            await bot.send_message(chat_id=admin, text='Бот остановлен')
        except ChatNotFound as e:
            logging.exception(f'Admin chat was not found: {e}')


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
    )
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup, on_shutdown=on_shutdown)
