from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.settings import settings
from utils import async_generator


async def get_themes_menu_inline_markup() -> InlineKeyboardMarkup:
    """
    Creates a menu of buttons from a list of themes.
    :return:
    """
    markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    if settings.bots.themes:
        async for theme in async_generator(settings.bots.themes, 0):
            markup.add(InlineKeyboardButton(theme, callback_data=theme))

    return markup
