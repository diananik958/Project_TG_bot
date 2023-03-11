import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram import types
from datetime import datetime
from dotenv import load_dotenv
import os

from AppExceptions import AppExceptions
from sql.add_user import add_user
from sql.check_registration import check_user
from sql.create_table import create_table
from sql.update_user import update_user


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
load_dotenv()
bot = Bot(token=os.getenv("BOT_API_KEY"))
dp = Dispatcher(bot)

# corporate domain that is used for emails
DOMAIN = os.getenv("DOMAIN")

# START---------------------------------------------------------------------------------------------

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        add_user(message.from_user.id, message.from_user.id, message.chat.id)
        await message.answer("Добрый день\nЯ бот, который должен помочь тебе повысить твои знания в фишинге."
                             "\nНо для начала тебе нужно зарегестрироваться")
    except AppExceptions.UserAlreadyExist as error:
        print(error)
        await message.answer(
            "Добрый день\nЯ бот, который должен помочь тебе повысить твои знания в фишинге."
                             "\nВы уже зарегестрированы, может изучить теорию или пройти тест.")
    except Exception as e:
        print(e)
        print("Unexpected error!")
        await message.answer(
            "Добрый день\nЯ бот, который должен помочь тебе повысить твои знания в фишинге."
            "\nЧто-то пошло не так ")


# HELP---------------------------------------------------------------------------------------------

@dp.message_handler(commands=['help'])
async def helpMSG(message: types.Message):
    text = (
        "/reg - зарегестрироваться, надо ввести корпоративный email"
        "/theory - теория"
        "/test - пройти тест"
        "/help - инструкция")
    await message.answer(text)


# REGISTRATION---------------------------------------------------------------------------------------------

@dp.message_handler(commands=['reg'])
async def register(message: types.Message):
    data = message.text[5:].split(' ')
    check_email = data[0].split('@')
    if check_email[1] == 'nstu.ru':
        try:
            update_user(message.from_user.id, data[0])
            print(message.from_user.id, data[0])
            await message.answer("Введен корректный адрес эл. почты. Вы успешно зарегестрированы")
        except AppExceptions.CantUpdateUserData as error:
            print(error)
            await message.answer("Что-то пошло не так :(")
    else:
        await message.answer("Введен некорректный адрес эл. почты, попробуйте еще раз")


# FOR INCORRECT COMMANDS---------------------------------------------------------------------------------------------
@dp.message_handler()
async def unknown(message: types.Message):
    await message.answer("Я тебя не понимаю, сорямба")


if __name__ == '__main__':
    create_table()
    executor.start_polling(dp, skip_updates=True)

