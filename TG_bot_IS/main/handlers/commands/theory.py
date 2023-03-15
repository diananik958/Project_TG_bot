import logging
from aiogram import Bot, Dispatcher
from aiogram import types
import os
from aiogram.dispatcher.filters import Command

from TG_bot_IS.loader import dp


@dp.message_handler(Command('theory'))
async def theory(message: types.Message):
    text_to_send = "Теорию по теме Фишинг можете изучить по ссылке:\nhttps://telegra.ph/Fishing-03-11"
    await message.answer(text_to_send)
