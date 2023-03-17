from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import os


from TG_bot_IS.AppExceptions import AppExceptions
from TG_bot_IS.sql.sqlite3.add_user import add_user
from TG_bot_IS.sql.sqlite3.check_registration import check_user
from TG_bot_IS.loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_exists = check_user(message.from_user.id)
    print(user_exists)
    if user_exists == 'None':
        try:
            add_user(message.from_user.id, message.from_user.id, message.chat.id)
            await message.answer(
                f"Добрый день, {message.from_user.first_name}!\nЯ бот, который должен помочь тебе повысить знания в фишинге."
                "\nНо для начала тебе нужно зарегистрироваться.\nДля этого введите команду /reg"
                " в формате /reg ваш_адрес@nstu.ru")
        except AppExceptions.UserAlreadyExist as error:
            print(error)
            await message.answer(
                f"Добрый день, {message.from_user.first_name}!Я бот, который должен помочь тебе повысить знания в фишинге."
                "\nЧто-то пошло не так.")
        except Exception as e:
            print(e)
            print("Unexpected error!")
            await message.answer(
                "Добрый день\nЯ бот, который должен помочь тебе повысить знания в фишинге."
                "\nЧто-то пошло не так...")
    else:
        await message.answer(
            f"Добрый день, {message.from_user.first_name}!\nЯ бот, который должен помочь тебе повысить знания в фишинге."
            "\nЕсли нужна помощь нажмите /help")
