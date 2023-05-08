from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_default_menu_inline_markup() -> InlineKeyboardMarkup:
    """
    Creates buttons for standard menus.
    :return:
    """
    markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    markup.add(InlineKeyboardButton(text='Подобрать группу', callback_data='select_theme'))
    markup.add(InlineKeyboardButton(text='Список групп', callback_data='list_groups'))

    return markup
