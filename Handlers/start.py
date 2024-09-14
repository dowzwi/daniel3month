from config import bot,dp
from aiogram import Dispatcher, types

async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello{message.from_user.first_name}')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start")