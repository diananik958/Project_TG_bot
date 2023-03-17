from aiogram import executor

from main.utils.set_bot_commands import set_default_commands

from sql.sqlite3.create_table import create_table

from TG_bot_IS.loader import dp


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    create_table()
    executor.start_polling(dp, on_startup=on_startup)
