from aiogram.types import CallbackQuery

from keyboards.inline import (
    get_back_to_menu_inline_markup,
    get_link_inline_markup
)
from loader import dp
from data.settings import settings
from services import get_groups
from utils import async_generator


@dp.callback_query_handler(text='list_groups')
async def list_all_groups_callback_handler(call: CallbackQuery):
    """
    Outputs a list of groups from the database.
    :param call:
    :return: list of groups view
    """
    answer = await call.message.answer('Формируем список групп...')
    groups = await get_groups()
    await answer.edit_text(text=f'Список групп:')

    async for group in async_generator(groups, settings.bots.message_delay):
        await call.message.answer(text=f'Название: {group.name}\nТематика: {group.theme}',
                                  reply_markup=await get_link_inline_markup(group.link))

    await call.message.answer(text='Это все группы на сегодня', reply_markup=await get_back_to_menu_inline_markup())
    await call.answer()
