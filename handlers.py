import asyncio
from aiogram import Bot, Router, types, F
from aiogram.fsm.context import FSMContext

from config import TOKEN, ALLOWED_USERS
from keyboards import yes_no_kb, master_kb_bot
from states import RepostDataToChat
from commands import GROUP_CHAT


router = Router()
bot = Bot(TOKEN)


# Блок хэндлеров для репоста сообщений в чат
@router.message(F.text == 'Сообщение')
async def input_msg_to_chat(msg: types.Message, state: FSMContext):
    if msg.chat.type == 'private':
            if msg.from_user.id in ALLOWED_USERS:
                await msg.answer(f'Напиши мне текст, который хочешь переслать в чат')
                await state.set_state(RepostDataToChat.input_text)

@router.message(RepostDataToChat.input_text, F.text)
async def confirm_msg_to_chat(msg: types.Message, state: FSMContext):
    text=msg.text
    await state.update_data(text=text)
    await msg.answer('Ты уверен в отправке?', reply_markup=yes_no_kb)
    await state.set_state(RepostDataToChat.confirm_text)

@router.message(RepostDataToChat.confirm_text)
async def send_msg_to_chat(msg: types.Message, state: FSMContext):
    if msg.text == 'Да':
        data = await state.get_data()
        text = data.get('text')
        await bot.send_message(GROUP_CHAT, text=text)
        await msg.answer('Сообщение успешно отправлено в чат')
        await asyncio.sleep(1)
        await msg.answer('Выбери действие:', reply_markup=master_kb_bot)
    else:
        await msg.answer('Отправка сообщения отменена')
        await asyncio.sleep(1)
        await msg.answer('Выбери действие:', reply_markup=master_kb_bot)
    await state.clear()


# Блок хэндлеров для репоста медиафайлов в чат
@router.message(F.text == 'Медиа')
async def input_media_to_chat(msg: types.Message, state: FSMContext):
    if msg.chat.type == 'private':
            if msg.from_user.id in ALLOWED_USERS:
                await msg.answer('Пришли мне медиафайл, который хочешь переслать в чат')
                await state.set_state(RepostDataToChat.input_media)

@router.message(RepostDataToChat.input_media, F.photo | F.audio | F.video | F.animation)
async def send_media_to_chat(msg: types.Message, state: FSMContext):
    content_type = msg.content_type
    if content_type == 'photo':
        await bot.send_photo(GROUP_CHAT, msg.photo[-1].file_id)
    elif content_type == 'video':
        await bot.send_video(GROUP_CHAT, msg.video.file_id)
    elif content_type == 'animation':
        await bot.send_animation(GROUP_CHAT, msg.animation.file_id)
    elif content_type == 'audio':
        await bot.send_audio(GROUP_CHAT, msg.audio.file_id)
    await asyncio.sleep(1)
    await msg.answer('Выбери действие:', reply_markup=master_kb_bot)
    await state.clear()