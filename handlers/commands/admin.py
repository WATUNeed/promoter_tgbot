import logging

from aiogram.types import Message

from keyboards.inline import get_admin_panel_inline_markup
from loader import dp


@dp.message_handler(is_admin=True, commands=['admin'])
async def admin_command_handler(msg: Message):
    """
    Running the admin panel.
    :param msg:
    :return:
    """
    logging.info(
        f'User {msg.from_user.full_name} with id {msg.from_user.id} logged into the admin panel.'
    )

    await msg.answer(f'Hi, {msg.from_user.full_name}!', reply_markup=await get_admin_panel_inline_markup())
