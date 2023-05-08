from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_back_to_menu_inline_markup() -> InlineKeyboardMarkup:
    """
    Creates a button to return to the menu.
    :return:
    """
    markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    markup.add(InlineKeyboardButton(text='Вернуться в меню', callback_data='back_to_menu'))

    return markup
