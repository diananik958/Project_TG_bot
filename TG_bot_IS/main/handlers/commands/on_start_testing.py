from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, InputFile

from TG_bot_IS.main.keyboards.inline.choice_but_start_test import towers_4, towers_2

from aiogram import types
from TG_bot_IS.main.states.on_start_test import CallbackOnStart

from TG_bot_IS.loader import dp


RESULT = []

@dp.message_handler(Command('onstarttest'))
async def tower(message: types.Message):
    keyboard = towers_4()
    await message.answer(text='<b>Вопрос №1</b>\nЧто из себя представляет фишинг в интернет пространстве?\n'
                         '<u>Выберите номер ответа:</u>\n'
                         '1. Интернет-мошенничество\n'
                         '2. Рыбалка онлайн\n'
                         '3. Завлечение новых пользователей\n'
                         '4. Реферальная программа по набору аудитории\n',
                         reply_markup=keyboard,parse_mode=types.ParseMode.HTML)
    await CallbackOnStart.Q1.set()


@dp.callback_query_handler(state=CallbackOnStart.Q1)
async def result1(call: types.CallbackQuery):
    answer = call.data
    if answer == "1":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №1:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №1:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q2)
async def on_start_test(message: types.Message):
    keyboard = towers_2()
    await message.answer_photo(InputFile('images/card.jpg'), '<b>Вопрос №2</b>\nВы покупаете рюкзак в интернет-магазине и переходите на страницу оплаты. Здесь всё в порядке? Можно платить?\n'
                         '<u>Выберите номер ответа:</u>\n'
                         '1. Да\n'
                         '2. Нет\n',
                         reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q2)
async def result2(call: types.CallbackQuery):
    answer = call.data
    if answer == "2":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №2:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №2:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q3)
async def tower(message: types.Message):
    keyboard = towers_4()
    await message.answer(text="<b>Вопрос №3</b>\nВ каком месте вы можете столкнуться с фишинговой ссылкой? \n<u>Выберите номер ответа:</u>\n"
                              "1. В сообщении от твоей мамы в ватсаппе\n"
                              "2. Рекламных записях пользователей VК\n"
                              "3. На сайте знакомств\n"
                              "4. Все варианты верны",
                         reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q3)
async def result3(call: types.CallbackQuery):
    answer = call.data
    if answer == "4":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №3:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №3:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q4)
async def on_start_test(message: types.Message):
    keyboard = towers_2()
    await message.answer_photo(InputFile('images/bank.jpg'), '<b>Вопрос №4</b>\nВам пришло СМС-сообщение от банка. Ему можно доверять?\n'
                         '<u>Выберите номер ответа:</u>\n'
                         '1. Да\n'
                         '2. Нет\n',
                         reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q4)
async def result4(call: types.CallbackQuery):
    answer = call.data
    if answer == "1":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №4:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №4:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q5)
async def tower(message: types.Message):
    keyboard = towers_4()
    await message.answer(text="<b>Вопрос №5</b>\nПри переходе на сайт с новинками кино и сайт с пиратской версией новой игры "
                           "браузер выдает сообщение, что сайт является опасным. Являются ли эти сайты фишинговыми? "
                           "\n<u>Выберите номер ответа:</u>\n"
                              "1. Да, оба\n"
                              "2. Да, с новинками кино\n"
                              "3. Да, с пиратской версией новой игры\n"
                              "4. Нет",
                            reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q5)
async def result2(call: types.CallbackQuery):
    answer = call.data
    if answer == "1":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №5:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №5:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()

@dp.message_handler(state=CallbackOnStart.Q6)
async def on_start_test(message: types.Message):
    keyboard = towers_2()
    await message.answer_photo(InputFile('images/message_from_bank.jpg'), '<b>Вопрос №6</b>\nВы получили такое письмо из банка. Откроете файл с подробностями?\n'
                         '<u>Выберите номер ответа:</u>\n'
                         '1. Да\n'
                         '2. Нет\n',
                         reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q6)
async def result4(call: types.CallbackQuery):
    answer = call.data
    if answer == "2":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №6:\n"
                                       "верный :)", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №6:\n"
                                        "неверный :(", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q7)
async def tower(message: types.Message):
    keyboard = towers_4()
    await message.answer(text="<b>Вопрос №7</b>\nВы заказали диплом за 3999 рублей на сайте DiplomLegko.ru и вам через неделю приходит на почту сообщение"
                         "о готовности работы, ссылки на оплату и rar архив с паролем, который вы получите после оплаты (пароль 1111). Ваши действия?"
                           "\n<u>Выберите номер ответа:</u>\n"
                              "1. Перейду по ссылке и укажу данные своей банковской карты\n"
                              "2. Подберу пароль для архива и запущу exe файл\n"
                              "3. Закажу диплом в другом месте  за 2999 рублей\n"
                              "4. Ничего из вышеперечисленного и напишу диплом сам",
                            reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(state=CallbackOnStart.Q7)
async def end(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    if answer == "4":
        await call.message.answer(text="Ваш ответ на вопрос №7:\n"
                                       "верный :)\n<b>Тест закончен</b>", reply_markup=ReplyKeyboardRemove(),
                                        parse_mode=types.ParseMode.HTML)
        RESULT.append(1)
    else:
        await call.message.answer(text="Ваш ответ на вопрос №7:\n"
                                       "неверный :(\n<b>Тест закончен</b>", reply_markup=ReplyKeyboardRemove(),
                                        parse_mode=types.ParseMode.HTML)
        RESULT.append(0)
    print(RESULT)
    if sum(RESULT) >= 5:
        await call.message.answer(
            text=f"Ваш результат: {sum(RESULT)}/10 (Успешно)", reply_markup=ReplyKeyboardRemove())
    else:
        await call.message.answer(
            text=f"Ваш результат: {sum(RESULT)}/10 (Неудовлетворительно, пройдите тест еще раз)",
            reply_markup=ReplyKeyboardRemove())
    await state.finish()
