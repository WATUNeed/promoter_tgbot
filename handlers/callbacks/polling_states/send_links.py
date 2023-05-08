from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.inline import (
    get_back_to_menu_inline_markup,
    get_link_inline_markup
)
from loader import dp
from data.settings import settings
from services.group_logic import get_groups_by_theme
from states import QuestionStatesMachine
from utils import async_generator


@dp.callback_query_handler(lambda call: call.data in settings.bots.themes, state=QuestionStatesMachine.send_links)
async def groups_by_theme_callback_handler(call: CallbackQuery, state: FSMContext):
    """
    Displays a list of groups by theme.
    :param call:
    :param state:
    :return: list of groups by theme
    """
    await call.message.delete()
    answer = await call.message.answer('Формируем список групп...')
    groups = await get_groups_by_theme(call.data)
    await answer.edit_text(text=f'Группы по теме "{call.data}":')

    async for group in async_generator(groups, settings.bots.message_delay):
        await call.message.answer(text=f'Название: {group.name}', reply_markup=await get_link_inline_markup(group.link))

    await call.message.answer(text='Это все группы на сегодня', reply_markup=await get_back_to_menu_inline_markup())
    await state.finish()
    await call.answer()
