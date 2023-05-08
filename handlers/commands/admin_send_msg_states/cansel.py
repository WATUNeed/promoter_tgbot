import logging

from aiogram.dispatcher import FSMContext
from aiogram.types.message import Message

from keyboards.inline import get_admin_panel_inline_markup
from loader import dp
from states import AdminSendMessageStatesMachine


@dp.message_handler(commands=['cancel'], is_admin=True, state=AdminSendMessageStatesMachine.wait_message)
async def send_msg_by_admin_message_handler(msg: Message, state: FSMContext):
    logging.info(
        f'User: "{msg.from_user.full_name}" with user_id: "{msg.from_user.id}"'
        f' cancelled the mailing list.'
    )

    await state.finish()
    await msg.answer(f'Рассылка отменена', reply_markup=await get_admin_panel_inline_markup())
