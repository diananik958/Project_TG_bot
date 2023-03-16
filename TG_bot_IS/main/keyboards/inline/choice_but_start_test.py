from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def towers_4():
    list_button_name = [['1', '3'],
                        ['2', '4']]

    buttons_list = []
    for item in list_button_name:
        l = []
        for i in item:
            l.append(InlineKeyboardButton(text=i, callback_data=i))
        buttons_list.append(l)

    keyboard_inline_buttons = InlineKeyboardMarkup(inline_keyboard=buttons_list)
    return keyboard_inline_buttons

def towers_2():
    list_button_name = [['1', '2'],
                        []]

    buttons_list = []
    for item in list_button_name:
        l = []
        for i in item:
            l.append(InlineKeyboardButton(text=i, callback_data=i))
        buttons_list.append(l)

    keyboard_inline_buttons = InlineKeyboardMarkup(inline_keyboard=buttons_list)
    return keyboard_inline_buttons
