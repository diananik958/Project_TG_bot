from aiogram import Bot, Dispatcher, executor

import main.handlers
from main.utils.set_bot_commands import set_default_commands


from TG_bot_IS.loader import dp


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
