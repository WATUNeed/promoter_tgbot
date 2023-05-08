from aiogram.types import Message

from loader import dp


@dp.message_handler(state='*')
async def incorrect_cmd_for_state_message_handler(msg: Message):
    await msg.answer('Неверная команда для этого состояния')
