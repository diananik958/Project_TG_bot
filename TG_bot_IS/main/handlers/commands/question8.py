"""
@dp.message_handler(state=CallbackOnStart.Q8)
async def on_start_test(message: types.Message):
    keyboard = towers_2()
    await message.answer_photo((InputFile'images/corona_mail.jpg'), '<b>Вопрос №8</b>\nВы получили актуальное письмо от знакомой интернет-аптеки с полезными рекомендациями по профилактике вирусов. Что вы сделаете?\n'
                         '<u>Выберите номер ответа:</u>\n'
                         '1. Кликну по ссылке! Интересно, да еще и маски дома закончились\n'
                         '2. Проигнорирую письмо и отправлю его в папку «Спам»\n',
                         reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q8)
async def result4(call: types.CallbackQuery):
    answer = call.data
    if answer == "2":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №8:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №8:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()
"""
