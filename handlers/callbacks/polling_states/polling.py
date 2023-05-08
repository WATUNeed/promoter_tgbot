from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.inline import get_choice_yes_or_no_menu_inline_markup
from loader import dp
from data.settings import settings
from services import get_questions_by_theme
from states import QuestionStatesMachine


@dp.callback_query_handler(lambda call: call.data in settings.bots.themes, state=QuestionStatesMachine.polling)
async def select_answer_for_question_callback_handler(call: CallbackQuery, state: FSMContext):
    """
    Launches on themes in a polling state.
    Polls the user on all questions on a given topic.
    :param call:
    :param state:
    :return: When the questions run out, changes state to send_links.
    """
    async with state.proxy() as data:
        if call.data not in data:
            data[call.data] = await get_questions_by_theme(call.data)
        else:
            await call.message.delete()

        question = data[call.data].pop()
        await call.message.answer(question.question, reply_markup=await get_choice_yes_or_no_menu_inline_markup(call))

        if len(data[call.data]) == 0:
            await QuestionStatesMachine.send_links.set()

    await call.answer(text='Ваше мнение для меня очень важно, но не очень то и нужно.')
