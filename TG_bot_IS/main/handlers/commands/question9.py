"""
@dp.message_handler(state=CallbackOnStart.Q9)
async def tower(message: types.Message):
    keyboard = towers_4()
    await message.answer(text="<b>Вопрос №9</b>\nКакой способ может помочь для защиты от фишинга? \n<u>Выберите номер ответа:</u>\n"
                              "1. Как можно меньше использовать собственный интернет и отдавать предпочтение общественному Wi-Fi\n"
                              "2. Обращать внимание на сертификат безопасности\n"
                              "3. Не обновлять ПО роутера\n"
                              "4. Все варианты верны",
                         reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q9)
async def result9(call: types.CallbackQuery):
    answer = call.data
    if answer == "2":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №9:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №9:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()
"""