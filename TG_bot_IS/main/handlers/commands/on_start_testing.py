from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from TG_bot_IS.main.keyboards.inline.choice_but_start_test import towers

from aiogram import types
from TG_bot_IS.main.states.on_start_test import CallbackOnStart

from TG_bot_IS.loader import dp

RESULT = []

@dp.message_handler(Command('onstarttest'))
async def on_start_test(message: types.Message):
    keyboard = towers()
    await message.answer('Вопрос №1\nЧто из себя представляет фишинг в интернет пространстве?\nВыберите номер ответа\n'
                         '1. интернет-мошенничество\n'
                         '2. рыбалка онлайн\n'
                         '3. завлечение новых пользователей\n'
                         '4. реферальная программа по набору аудитории',
                         reply_markup=keyboard)
    await CallbackOnStart.Q1.set()


@dp.callback_query_handler(state=CallbackOnStart.Q1)
async def result1(call: types.CallbackQuery):
    answer = call.data
    if answer == "1":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №1:\n"
                                       "верный", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №1:\n"
                                        "неверный", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q2)
async def tower(message: types.Message):
    keyboard = towers()
    await message.answer(text="Вопрос №2\nВ каком месте вы можете столкнуться с фишинговой ссылкой? \nВыберите номер ответа\n"
                              "1. в сообщении от твоей мамы в ватсаппе\n"
                              "2. рекламных записях пользователей VК\n"
                              "3. на сайте знакомств\n"
                              "4. все варианты верны",
                         reply_markup=keyboard)


@dp.callback_query_handler(state=CallbackOnStart.Q2)
async def result2(call: types.CallbackQuery):
    answer = call.data
    if answer == "4":
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №2:\n"
                                       "верный", reply_markup=ReplyKeyboardRemove())
        RESULT.append(1)
    else:
        await call.message.answer(text="Следующий вопрос: /onstarttest\nВаш ответ на вопрос №2:\n"
                                        "неверный", reply_markup=ReplyKeyboardRemove())
        RESULT.append(0)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q3)
async def tower(call: types.Message):
    keyboard = towers()
    await call.answer(text="Вопрос №3\nПри переходе на сайт с новинками кино и сайт с пиратской версией новой игры "
                           "браузер выдает сообщение, что сайт является опасным. Являются ли эти сайты фишинговыми? "
                           "\nВыберите номер ответа\n"
                              "1. Да, оба\n"
                              "2. Да, с новинками кино\n"
                              "3. Да, с пиратской версией новой игры\n"
                              "4. Нет",
                            reply_markup=keyboard)


@dp.callback_query_handler(state=CallbackOnStart.Q3)
async def end(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    if answer == "1":
        await call.message.answer(text="Ваш ответ на вопрос №3:\n"
                                       "верный\nТест закончен", reply_markup=ReplyKeyboardRemove(),
                                        parse_mode=types.ParseMode.HTML)
        RESULT.append(1)
    else:
        await call.message.answer(text="Ваш ответ на вопрос №3:\n"
                                       "неверный\n<b>Тест закончен</b>", reply_markup=ReplyKeyboardRemove(),
                                        parse_mode=types.ParseMode.HTML)
        RESULT.append(0)
    print(RESULT)
    if sum(RESULT) > 5:
        await call.message.answer(
            text=f"Ваш результат: {sum(RESULT)}/10 (Успешно)", reply_markup=ReplyKeyboardRemove())
    else:
        await call.message.answer(
            text=f"Ваш результат: {sum(RESULT)}/10 (Неудовлетворительно, пройдите тест еще раз)",
            reply_markup=ReplyKeyboardRemove())
    await state.finish()

