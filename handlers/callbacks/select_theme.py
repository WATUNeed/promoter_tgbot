from aiogram.types import CallbackQuery

from keyboards.inline import get_themes_menu_inline_markup
from loader import dp
from states import QuestionStatesMachine


@dp.callback_query_handler(text='select_theme')
async def select_themes_callback_handler(call: CallbackQuery):
    """
    Chooses the theme of the groups
    :param call:
    :return: Launches a survey on the theme
    """
    await QuestionStatesMachine.polling_standby.set()
    await call.message.answer(
        text=f'Чем интересуетесь?',
        disable_web_page_preview=True,
        reply_markup=await get_themes_menu_inline_markup()
    )
    await call.answer()
