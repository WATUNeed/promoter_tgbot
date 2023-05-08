import logging

from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import ChatNotFound, ChatIdIsEmpty

from keyboards.inline import get_admin_panel_inline_markup
from services import get_users
from states import AdminSendMessageStatesMachine
from loader import dp, bot
from data.settings import settings
from utils import async_generator


@dp.message_handler(is_admin=True, state=AdminSendMessageStatesMachine.wait_message)
async def send_msg_by_admin_message_handler(msg: Message, state: FSMContext):
    """
    Send messages to all users in the admin panel.
    :param msg:
    :param state:
    :return:
    """
    logging.info(
        f'User: "{msg.from_user.full_name}" with user_id: "{msg.from_user.id}"'
        f' sent out a message to all users: "{msg.text}".'
    )

    users = await get_users()

    if users:
        async for user in async_generator(users, settings.bots.message_delay):
            try:
                await bot.send_message(chat_id=user.user_id, text=msg.text)
            except ChatNotFound as e:
                logging.info(f'Chat_id {user.user_id} was not found: {e}')
            except ChatIdIsEmpty as e:
                logging.info(f'Chat_id {user.user_id} is empty: {e}')

    await state.finish()
    await msg.answer(f'Рассылка завершена', reply_markup=await get_admin_panel_inline_markup())
