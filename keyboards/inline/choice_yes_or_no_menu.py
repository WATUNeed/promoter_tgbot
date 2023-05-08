from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_choice_yes_or_no_menu_inline_markup(call: CallbackQuery) -> InlineKeyboardMarkup:
    """
    Creates buttons with a choice of 'Yes' or 'No'.
    :param call: callback_data data
    :return:
    """
    markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)

    # TODO В тз не было прописано что должны делать эти кнопки. Сейчас они в виде загрушки.
    markup.row(
        InlineKeyboardButton('Да', callback_data=call.data),
        InlineKeyboardButton('Нет', callback_data=call.data)
    )

    return markup
