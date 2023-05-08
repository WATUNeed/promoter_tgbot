import logging

from aiogram.types import CallbackQuery

from states import AdminSendMessageStatesMachine
from loader import dp


@dp.callback_query_handler(text='send_message', is_admin=True)
async def input_msg_by_admin_callback_handler(call: CallbackQuery):
    """
    Request to the admin to enter a wait_message to send to all users.
    :param call:
    :return:
    """
    logging.info(
        f'User: "{call.from_user.full_name}" with user_id: "{call.from_user.id}" requested a mailing list of users.'
    )

    await AdminSendMessageStatesMachine.wait_message.set()
    await call.message.answer(text=f'Введите сообщение для пользователей. Для отмены рассылки введите команду /cancel:')
    await call.answer()
