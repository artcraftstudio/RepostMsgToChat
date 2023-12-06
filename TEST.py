import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import TOKEN, TestBotGroup
from keyboards import master_kb_bot, yes_no_kb
from classes import RepostDataToChat

dp = Dispatcher()
bot = Bot(TOKEN)

@dp.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    await msg.answer('Это тест. Выбери действие:', reply_markup=master_kb_bot)




@dp.message(F.text == 'Медиа')
async def input_media_to_chat(msg: types.Message, state: FSMContext):
    await msg.answer('Пришли мне медиафайл, который хочешь переслать в чат')
    await state.set_state(RepostDataToChat.input_media)

@dp.message(RepostDataToChat.input_media, F.photo | F.audio | F.video | F.animation)
async def cnfrm_media_to_chat(msg: types.Message, state: FSMContext):
    content_type = msg.content_type
    await state.update_data(content_type=content_type)
    await msg.answer('Ты уверен в отправке?', reply_markup=yes_no_kb)
    await state.set_state(RepostDataToChat.confirm_media)

# почему-то на этом этапе id медиафайла не передаётся из состояния выше в состояние ниже, и консоль выдаёт ошибку

@dp.message(RepostDataToChat.confirm_media)
async def send_media_to_chat(msg: types.Message, state: FSMContext):
    if msg.text == 'Да':
        data = await state.get_data()
        content_type = data.get('content_type')
        if content_type == 'photo':
            await bot.send_photo(TestBotGroup, msg.photo[-1].file_id)
        elif content_type == 'video':
            await bot.send_video(TestBotGroup, msg.video.file_id)
        elif content_type == 'animation':
            await bot.send_animation(TestBotGroup, msg.animation.file_id)
        elif content_type == 'audio':
            await bot.send_audio(TestBotGroup, msg.audio.file_id)
    else:
        await msg.answer('Отправка отменена')
        await asyncio.sleep(1)
        await msg.answer('Выбери действие:', reply_markup=master_kb_bot)
    await state.clear()






async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
