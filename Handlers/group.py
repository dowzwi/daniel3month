from aiogram.types import document
from config import dp, bot
from aiogram import types, Dispatcher

async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.reply_to_message:
            pinnes=message.reply_to_message
            await bot.pin_chat_message(message.chat.id,pinnes.message_id)
        else:
            await message.answer('couldnt pin')
    else:
        await message.answer('work only in open groups')

def register_group(dp: Dispatcher):
    dp.register_message_handler(pin,text='!pin')