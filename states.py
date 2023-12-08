from aiogram.fsm.state import State, StatesGroup


class RepostDataToChat(StatesGroup):
    input_text = State()
    confirm_text = State()
    input_media = State()
    confirm_media = State()
