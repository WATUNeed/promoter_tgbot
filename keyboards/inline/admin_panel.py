from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_admin_panel_inline_markup() -> InlineKeyboardMarkup:
    """
    Creates buttons for the admin panel.
    :return:
    """
    markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    markup.add(InlineKeyboardButton('Выгрузить пользователей', callback_data='dump_users'))
    markup.add(InlineKeyboardButton('Отправить сообщение пользователям', callback_data='send_message'))

    return markup
