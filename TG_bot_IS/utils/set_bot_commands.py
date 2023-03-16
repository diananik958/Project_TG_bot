from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Инструкция по работе с ботом"),
            types.BotCommand("onstarttest", "Пройти тест"),
            types.BotCommand("theory", "Команда для изучения теории по теме"),
            types.BotCommand("reg", "команда для регистрации в боте. Для начала обучения необходимо зарегистрироваться."
                                    "Введите команду в формате /reg ваш_адрес@nstu.ru")
        ]
    )
