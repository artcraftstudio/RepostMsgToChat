from aiogram import Router, types
from aiogram.filters import Command

from config import ALLOWED_USERS, TestChat1, TestChat2
from keyboards import master_kb_bot, user_kb_bot


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
        await msg.answer(
              'Привет! Переходи в групповой чат',
              reply_markup=user_kb_bot
        )

# здесь я пытался менять значение переменной с помощью команды и импортировать переменную GROUP_CHAT в другом файле. Но это не работает, GROUP_CHAT не импортируется
@router.message(Command('testchat1'))
async def testchat1(msg: types.Message) -> None:
    if msg.chat.type != 'private':
        return
    elif msg.from_user.id in ALLOWED_USERS:
        GROUP_CHAT = TestChat1
        await msg.reply('Переменной GROUP_CHAT присвоено значение TestChat1')

@router.message(Command('testchat2'))
async def chat(msg: types.Message) -> None:
    if msg.chat.type != 'private':
        return
    elif msg.from_user.id in ALLOWED_USERS:
        GROUP_CHAT = TestChat2
        await msg.reply('Переменной GROUP_CHAT присвоено значение TestChat2')
