from telebot import types

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Погода🌤', request_location= True)
source_markup_btn2 = types.KeyboardButton('Гороскоп🔮')
source_markup.add(source_markup_btn1, source_markup_btn2)
source_markup_bt3 = types.KeyboardButton('Курс валют💰')
source_markup_bt4 = types.KeyboardButton('Фильм🎬')
source_markup.add(source_markup_bt3, source_markup_bt4)
