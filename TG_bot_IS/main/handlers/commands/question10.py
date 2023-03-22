"""
@dp.message_handler(state=CallbackOnStart.Q10)
async def on_start_test(message: types.Message):
    keyboard = towers_2()
    await message.answer_photo((InputFile'images/exchange.jpg'), '<b>Вопрос №10</b>\nВы решили избавиться от ненужных вещей и пытаетесь продать их на известном сайте с объявлениями. Вам приходит такое сообщение. Что будете делать?\n'
                         '<u>Выберите номер ответа:</u>\n'
                         '1. Кликну по ссылке — вдруг там выгодное предложение?\n'
                         '2. Не буду переходить по ссылке и удалю сообщение\n',
                         reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q10)
async def result10(call: types.CallbackQuery):
    answer = call.data
    if answer == "2":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №10:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №10:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()
"""
