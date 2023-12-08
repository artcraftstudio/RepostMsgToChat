from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# админская основная клавиатура
builder1 = ReplyKeyboardBuilder()
builder1.add(KeyboardButton(text='Сообщение'))
builder1.add(KeyboardButton(text='Медиа'))
builder1.adjust(2)
master_kb_bot = builder1.as_markup(resize_keyboard=True, one_time_keyboard=True)

# Клавивиатура Да/Нет
builder2 = ReplyKeyboardBuilder()
builder2.add(KeyboardButton(text='Да'))
builder2.add(KeyboardButton(text='Нет'))
builder2.adjust(2)
yes_no_kb = builder2.as_markup(resize_keyboard=True, one_time_keyboard=True)
