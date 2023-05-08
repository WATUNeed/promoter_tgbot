from aiogram.types import CallbackQuery

from loader import dp


@dp.callback_query_handler(state='*')
async def incorrect_btn_for_state_callback_handler(call: CallbackQuery):
    await call.answer('Неверная кнопка для этого состояния')
