from aiogram.types import Message

from filters import AdminFilter
from keyboards.inline import get_default_menu_inline_markup
from loader import dp
from services import create_user


@dp.message_handler(commands=['start'])
async def start_command_handler(msg: Message):
    """
    Sends an initial wait_message.
    :param msg:
    :return:
    """
    await create_user(
        user_id=str(msg.from_user.id),
        full_name=msg.from_user.full_name,
        is_admin=await AdminFilter(msg).check(msg)
    )
    await msg.answer(text=f'Привет! Я бот, который поможет тебе выбрать группу по твоим интересам',
                     reply_markup=await get_default_menu_inline_markup())
