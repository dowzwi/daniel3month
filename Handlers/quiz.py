from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot,dp


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    butt1 = InlineKeyboardButton('next', callback_data='next1')
    markup.add(butt1)

    question = 'BMW or Mercedes?'
    answer = ['BMW', 'Mercedes']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Кыргызский автопром!',
        open_period=60,
        reply_markup=markup
    )


async def question_2(call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    butt1 = InlineKeyboardButton('next', callback_data='next2')
    markup.add(butt1)
    question = 'What is your favorite city?'
    answer = ['NYC', 'Bishkek']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Наш слоняра!',
        open_period=60,
        reply_markup=markup
    )


async def question_3(call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    butt1 = InlineKeyboardButton('next', callback_data='next3')
    markup.add(butt1)
    question = 'Сколько мне лет?'
    answer = ['15','16']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation='Правильно! ',
        open_period=60,
    )


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(question_2, text='next1')
    dp.register_callback_query_handler(question_3, text='next2')