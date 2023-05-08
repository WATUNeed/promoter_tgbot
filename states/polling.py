from aiogram.dispatcher.filters.state import State, StatesGroup


class QuestionStatesMachine(StatesGroup):
    """
    :param polling_standby: Polling standby status
    :param polling: In the process of asking questions.
    :param send_links: The questions are over, the send links can be given out.
    """
    polling_standby = State()
    polling = State()
    send_links = State()
