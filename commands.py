from aiogram import Router, types
from aiogram.filters import Command

from config import ALLOWED_USERS
from keyboards import master_kb_bot


router = Router()


@router.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    if msg.chat.type != 'private':
        return
    elif msg.from_user.id in ALLOWED_USERS:
        await msg.answer(
            'Привет!\n'
            'Выбери действие для чата:',
            reply_markup=master_kb_bot
        )
    else:
        await msg.answer('Привет!')
