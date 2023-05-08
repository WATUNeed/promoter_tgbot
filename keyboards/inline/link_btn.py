from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_link_inline_markup(url: str) -> InlineKeyboardMarkup:
    """
    Creates a button with a link.
    :param url: jump to link
    :return:
    """
    markup = InlineKeyboardMarkup(resize_keyboard=True)

    markup.add(InlineKeyboardButton('Ссылка', url=url))

    return markup
