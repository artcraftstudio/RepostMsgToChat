from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


builder3 = ReplyKeyboardBuilder()
builder3.add(KeyboardButton(text='Написать сбщ в чат'))
builder3.add(KeyboardButton(text='Тестовая кнопка'))
builder3.adjust(2)
main_kb_bot = builder3.as_markup(one_time_keyboard=True)


builder4 = ReplyKeyboardBuilder()
builder4.add(KeyboardButton(text='Да'))
builder4.add(KeyboardButton(text='Нет'))
builder4.adjust(2)
yes_no_kb = builder4.as_markup(one_time_keyboard=True)


builder5 = ReplyKeyboardBuilder()
builder5.add(KeyboardButton(text='TestChat1'))
builder5.add(KeyboardButton(text='TestChat2'))
builder4.adjust(2)
choose_chat_kb = builder5.as_markup(one_time_keyboard=True)