import logging
from aiogram import Bot, Dispatcher
from aiogram import types

from dotenv import load_dotenv
import os

from aiogram.dispatcher.filters import Command


from TG_bot_IS.sql.update_user import update_user
from TG_bot_IS.sql.check_registration import check_user

from TG_bot_IS.loader import dp

load_dotenv()

# corporate domain that is used for emails
DOMAIN = os.getenv("DOMAIN")


@dp.message_handler(Command('reg'))
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
                except AssertionError as error:
                    print(error)
                    await message.answer("Что-то пошло не так :(")
            else:
                await message.answer("Вы уже зарегестрированы")
        else:
            await message.answer("Введен некорректный адрес эл. почты, попробуйте еще раз")
