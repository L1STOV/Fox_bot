from telebot import types
from telebot.types import InlineKeyboardButton

inline_markup = types.InlineKeyboardMarkup(row_width=3)

inline_btn1 = InlineKeyboardButton(text='♈Овен', callback_data='Овен')
inline_btn2 = InlineKeyboardButton(text='♊Близнецы', callback_data='Близнецы')
inline_markup.add(inline_btn1, inline_btn2)
inline_btn3 = InlineKeyboardButton(text='♉Телец', callback_data='Телец')
inline_btn4 = InlineKeyboardButton(text='♋Рак', callback_data='Рак')
inline_markup.add(inline_btn3, inline_btn4)
inline_btn5 = InlineKeyboardButton(text='♌Лев', callback_data='Лев')
inline_btn6 = InlineKeyboardButton(text='♍Дева', callback_data='Дева')
inline_markup.add(inline_btn5, inline_btn6)
inline_btn7 = InlineKeyboardButton(text='♎Весы', callback_data='Весы')
inline_btn8 = InlineKeyboardButton(text='♏Скорпион', callback_data='Скорпион')
inline_markup.add(inline_btn7, inline_btn8)
inline_btn9 = InlineKeyboardButton(text='♐Стрелец', callback_data='Стрелец')
inline_btn10 = InlineKeyboardButton(text='♑Козерог', callback_data='Козерог')
inline_markup.add(inline_btn9, inline_btn10)
inline_btn11 = InlineKeyboardButton(text='♒Водолей', callback_data='Водолей')
inline_btn12 = InlineKeyboardButton(text='♓Рыбы', callback_data='Рыбы')
inline_markup.add(inline_btn11, inline_btn12)


