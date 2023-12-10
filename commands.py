from aiogram import Router, types
from aiogram.filters import Command

from config import ALLOWED_USERS, TestChat1, TestChat2
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

# идея в том, что после этой команды пользователю предлагается ввести значение. А дальше переменная импортируется в файле handlers
@router.message(Command('changechat'))
async def change_chat(msg: types.Message) -> None:
    global GROUP_CHAT
    await msg.reply('Введи значение переменной GROUP_CHAT:')
    GROUP_CHAT = await msg.get_args()
