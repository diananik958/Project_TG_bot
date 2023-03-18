from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from TG_bot_IS.loader import dp


@dp.message_handler(CommandHelp())
async def help_msg(message: types.Message):
    text = (
        "/reg - команда для регистрации в боте. Для начала обучения необходимо зарегистрироваться. Введите команду "
        "в формате /reg ваш_адрес@nstu.ru\n"
        "/theory - команда для изучения теории по теме\n"
        "/onstarttest - команда для изучения прохождения теста по теме\n"
        "/help - инструкция по работе с ботом")
    await message.answer(text)



