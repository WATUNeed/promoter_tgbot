from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from handlers.callbacks.polling_states.polling import select_answer_for_question_callback_handler
from loader import dp
from data.settings import settings
from states import QuestionStatesMachine


@dp.callback_query_handler(lambda call: call.data in settings.bots.themes, state=QuestionStatesMachine.polling_standby)
async def launch_survey_by_theme_callback_handler(call: CallbackQuery, state: FSMContext):
    """
    Launches a survey on the theme.
    :param call:
    :param state:
    :return:
    """
    await call.message.delete()
    await QuestionStatesMachine.polling.set()
    await select_answer_for_question_callback_handler(call, state)
    await call.answer()
