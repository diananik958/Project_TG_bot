from aiogram import types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import Command
from TG_bot_IS.loader import dp


@dp.message_handler(Command('theory'))
async def theory(message: types.Message):
    await message.answer(f"Теорию по теме Фишинг можете изучить по ссылке:{fmt.hide_link('https://telegra.ph/Fishing-03-11')}",
                         parse_mode=types.ParseMode.HTML)