from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminSendMessageStatesMachine(StatesGroup):
    """
    :param wait_message: Waiting for wait_message from admin to send out to users.
    """
    wait_message = State()
