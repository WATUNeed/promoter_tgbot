import logging

from aiogram.types import CallbackQuery

from loader import dp
from services import create_dump_users


@dp.callback_query_handler(text='dump_users', is_admin=True)
async def admin_request_for_dump_callback_handler(call: CallbackQuery):
    """
    Admin request for user dump.
    :param call:
    :return:
    """
    logging.info(
        f'User: "{call.from_user.full_name}" with user_id: "{call.from_user.id}" requested users uploads.'
    )

    try:
        filename = await create_dump_users()
        await call.answer(text=f'Файл дампа пользователей успешно создан: {filename}', show_alert=True)
    except Exception as e:
        logging.exception(f'Dumps of users error {e}')
        await call.answer(text=f'Ошибка в процессе создания дампа пользоваетей', show_alert=True)
