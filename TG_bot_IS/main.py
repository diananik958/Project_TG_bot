from aiogram import executor

from TG_bot_IS.utils.set_bot_commands import set_default_commands


from TG_bot_IS.loader import dp


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    try:
        print("trying await set_default_commands(dispatcher)")
        await set_default_commands(dispatcher)
        print("await set_default_commands(dispatcher)")
    except AssertionError as error:
        print(error)

if __name__ == '__main__':
    print("executor.start_polling(dp, on_startup=on_startup)")
    executor.start_polling(dp, on_startup=on_startup)

