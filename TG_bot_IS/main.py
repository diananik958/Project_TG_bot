import logging
from aiogram import Bot, Dispatcher, executor
from aiogram import types
from datetime import datetime
from dotenv import load_dotenv
import os

from AppExceptions import AppExceptions
from sql.add_user import add_user
from sql.create_table import create_table
from sql.update_user import update_user
from sql.check_registration import check_user


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
    user_exists = check_user(message.from_user.id)
    print(user_exists)
    if user_exists == 'None':
        try:
            add_user(message.from_user.id, message.from_user.id, message.chat.id)
            await message.answer(f"Добрый день, {message.from_user.first_name}!\nЯ бот, который должен помочь тебе повысить знания в фишинге."
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
        await message.answer(f"Добрый день, {message.from_user.first_name}!\nЯ бот, который должен помочь тебе повысить знания в фишинге."
                             "\nЕсли нужна помощь нажмите /help")

# HELP---------------------------------------------------------------------------------------------

@dp.message_handler(commands=['help'])
async def helpMSG(message: types.Message):
    text = (
        "/reg - команда для регистрации в боте. Для начала обучения необходимо зарегистрироваться. Введите команду "
        "в формате /reg ваш_адрес@nstu.ru\n"
        "/theory - команда для изучения теории по теме\n"
        "/test - команда для изучения прохождения теста по теме\n"
        "/help - инструкция по работе с ботом")
    await message.answer(text)


# REGISTRATION---------------------------------------------------------------------------------------------

@dp.message_handler(commands=['reg'])
async def register(message: types.Message):
    data = message.text[5:].split(' ')
    check_email = data[0].split('@')
    if len(check_email) != 2:
        await message.answer("Введен некорректный адрес эл. почты, попробуйте еще раз")
    else:
        if check_email[1] == 'nstu.ru':
            corpemail = check_user(message.from_user.id)[1:-1].split(', ')
            print(corpemail)
            if corpemail[2] == 'None':
                try:
                    update_user(message.from_user.id, data[0])
                    print(message.from_user.id, data[0])
                    await message.answer("Введен корректный адрес эл. почты. Вы успешно зарегестрированы")
                except AppExceptions.CantUpdateUserData as error:
                    print(error)
                    await message.answer("Что-то пошло не так :(")
            else:
                await message.answer("Вы уже зарегестрированы")
        else:
            await message.answer("Введен некорректный адрес эл. почты, попробуйте еще раз")

# REGISTRATION---------------------------------------------------------------------------------------------

@dp.message_handler(commands=['theory'])
async def theory(message: types.Message):
    text_to_send = "Теорию по теме Фишинг можете изучить по ссылке:\nhttps://telegra.ph/Fishing-03-11"
    await message.answer(text_to_send)


# REGISTRATION---------------------------------------------------------------------------------------------

@dp.message_handler(commands=['test'])
async def test(message: types.Message):
    await message.answer("Модуль в процессе разработки")


# FOR INCORRECT COMMANDS---------------------------------------------------------------------------------------------
@dp.message_handler()
async def unknown(message: types.Message):
    await message.answer("Я тебя не понимаю, сорямба")


if __name__ == '__main__':
    create_table()
    executor.start_polling(dp, skip_updates=True)

