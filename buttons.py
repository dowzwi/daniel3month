from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

# ===============================================================

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_buttons = KeyboardButton('/start')
mem_buttons = KeyboardButton('/mem')
mem_all_buttons = KeyboardButton('/mem_all')
music_buttons = KeyboardButton('/music')


start.add(start_buttons, mem_buttons, mem_all_buttons,
          music_buttons)

# ===============================================================

start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
KeyboardButton('/start')
)

# ===============================================================

start_test_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    )

start_test_1.add(
    KeyboardButton('/start'),
    KeyboardButton('/mem'),
    KeyboardButton('/mem_all'),
    KeyboardButton('/music')
)

# ===============================================================


cancel_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))

submit_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                    row_width=2).add(KeyboardButton('Да'), KeyboardButton('Нет'))


sizes = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('L'),
                                                            types.KeyboardButton('M'))
link='https://online.geeks.kg/'
web=types.WebAppInfo(url=link)
urls=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text='geeks',web_app=web),
                                      types.InlineKeyboardButton(text='geeks',web_app=web),
                                      types.InlineKeyboardButton(text='geeks',web_app=web),
                                      types.InlineKeyboardButton(text='geeks',web_app=web),
                                      types.InlineKeyboardButton(text='geeks',web_app=web),)
