from aiogram.fsm.state import State, StatesGroup


class RepostMsgToChat(StatesGroup):
    insert_text = State()
    confirm_text = State()
    choose_chat = State()