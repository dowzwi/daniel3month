import logging
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import os
from aiogram.types import InputFile

TOKEN = "7441664229:AAFBn_63GFbX2RqCYI6tj0f1oeXUprops4o"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

admin = [2091942960, ]


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello!')
    await message.answer(text='Привет')



@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    folder = 'media'

    photo_path = os.path.join(folder, 'img.jpeg')

    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo)



@dp.message_handler(commands=['mem_all'])
async def mem_all_handler(message: types.Message):
    folder = 'media'
    photos = os.listdir(folder)

    for photo_name in photos:
        photo_path = os.path.join(folder, photo_name)

        if photo_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            with open(photo_path, 'rb') as photo:
                await bot.send_photo(message.from_user.id, photo)



@dp.message_handler(commands=['music'])
async def music_handler(message: types.Message):
    folder = 'music'
    music_name = "track1.mp3"

    music_path = os.path.join(folder, music_name)
    with open (music_path, 'rb') as music:
        await message.answer_audio(music)

@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)