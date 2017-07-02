from telebot import types

def start_markup():

    keyboard = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(text="1. <Действие>", callback_data='btn1')
    btn2 = types.InlineKeyboardButton(text="2. <Действие>", callback_data='btn2')

    keyboard.add(btn1)
    keyboard.add(btn2)

    return keyboard

def btn1_markup():

    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="1.1 <Действие>", callback_data="btn1_1")
    btn2 = types.InlineKeyboardButton(text="1.2 <Действие>", callback_data="btn1_2")
    btn3 = types.InlineKeyboardButton(text="1.3 <Действие>", callback_data="btn1_3")
    btn4 = types.InlineKeyboardButton(text="<< Назад", callback_data="btn1_4")

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)

    return keyboard

def btn2_markup():
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="2.1 <Действие>", callback_data="btn2_1")
    btn2 = types.InlineKeyboardButton(text="2.2 <Действие>", callback_data="btn2_2")
    btn3 = types.InlineKeyboardButton(text="2.3 <Действие>", callback_data="btn2_3")
    btn4 = types.InlineKeyboardButton(text="<< Назад", callback_data="btn1_4")

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)

    return keyboard