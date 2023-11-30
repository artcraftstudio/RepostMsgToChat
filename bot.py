import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from config import TOKEN
from keyboards import main_kb_bot, yes_no_kb, choose_chat_kb
from lists import chats
from classes import RepostMsgToChat


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
        await message.answer(
            f'Привет!. Я могу отправить твое сообщение в чат\n'
            f'Посмотри команды на клавиатуре.',
            reply_markup=main_kb_bot
        )

@dp.message(F.text == 'Написать сбщ в чат')
async def choose_chat_msg_to_chat(message: types.Message, state: FSMContext):
    await message.answer('Выбери чат для отправки', reply_markup=choose_chat_kb)
    await state.set_state(RepostMsgToChat.choose_chat)

@dp.message(RepostMsgToChat.choose_chat)
async def receive_msg_to_chat(message: types.Message, state: FSMContext):
    if message.text in chats:
        await state.update_data(chat=message.text)
        await message.answer('Напиши мне текст, который хочешь переслать в чат')
        await state.set_state(RepostMsgToChat.insert_text)
    else:
        await message.answer('Отправка отменена', reply_markup=main_kb_bot)
        await state.clear()

@dp.message(RepostMsgToChat.insert_text)
async def confirm_msg_to_chat(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer('Ты уверен?', reply_markup=yes_no_kb)
    await state.set_state(RepostMsgToChat.confirm_text)

@dp.message(RepostMsgToChat.confirm_text, F.text == 'Да')
async def send_msg_to_chat(message: types.Message, state: FSMContext):
    data = await state.get_data()
    chat_id = await bot.get_chat(data['chat'])
    await bot.send_message(chat_id, data['text'])
    await message.answer('Сообщение успешно отправлено', reply_markup=main_kb_bot)
    await state.clear()

@dp.message(RepostMsgToChat.confirm_text, F.text == 'Нет')
async def cancel_msg_to_chat(message: types.Message, state: FSMContext):
    await message.answer('Отправка отменена', reply_markup=main_kb_bot)
    await state.clear()




async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())