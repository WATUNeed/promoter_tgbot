from aiogram.types import CallbackQuery

from keyboards.inline import get_default_menu_inline_markup
from loader import dp


@dp.callback_query_handler(text='back_to_menu')
async def back_main_menu_callback_handler(call: CallbackQuery):
    """
    Main menu after return.
    :param call:
    :return:
    """
    await call.message.delete()
    await call.message.answer(text=f'Выберите функцию', reply_markup=await get_default_menu_inline_markup())
    await call.answer()
