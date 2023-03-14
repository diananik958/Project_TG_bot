from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#INLINE ------------------------------------------------------------------------------------------------------------
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Теория по теме Фишинг', url='https://telegra.ph/Fishing-03-11')
urlkb.add(urlButton)

@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Теорию по теме Фишинг можете изучить по ссылке:', reply_markup=urlkb)

#REPLY -------------------------------------------------------------------------------------------------------------
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="/help"),
            types.KeyboardButton(text="/theory")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.reply("Выбери одну из представленных ниже команд:",
                        reply_markup=keyboard)