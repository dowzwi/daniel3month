import logging
from aiogram.utils import executor
from buttons import start_test
from config import bot, dp, admin
from Handlers import (commands, echo, quiz, FSM_registration, fsm_storage, webapp, admin_group,
                      send_products, send__delete_product)
from db import db_main


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=start_test)
        await db_main.sql_create()


commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_registration.register_fsm_reg(dp)
fsm_storage.register_store(dp)
webapp.register_handlers_webapp(dp)

send_products.register_send_products_handler(dp)
send__delete_product.register_send_delete_product(dp)


admin_group.register_admin_group(dp)
# echo.register_echo(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)