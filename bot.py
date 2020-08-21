import telebot
import config
import datetime
import random
import pyowm
import markup as m
from horoscope_parser import HoroscopeParser
from horoscope_parser import zodiaks
from cinema_parser import CinemaParser
from currency_parser import CurrencyParser
import inline_markup as im
import threading

# Weather
owm_api_key = config.owm_api_token
owm = pyowm.OWM(owm_api_key)
mgr = owm.weather_manager()

# Bot init
bot = telebot.TeleBot(config.tel_api_token)

# Horoscope parser
horoscope_parser = HoroscopeParser()

# Cinema parser
cinema_parser = CinemaParser()

# Cinema parser
currency_parser = CurrencyParser()


@bot.message_handler(content_types=['location', 'text'])
def fox_init(message):

    print('New bot command: '+message.text)
    print(message.chat.id)
    print(message.chat.first_name)
    print(message.chat.last_name)
    print(message.chat.username)
    print('\n')

    if message.text == "/start":
        chat_id = message.chat.id
        intro_msg = f"Привет , {message.from_user.first_name}👋🏻" \
                    "\nМеня зовут Фокс🦊 и я твой персональный помощник☺"
        msg = bot.send_message(message.chat.id, intro_msg)
        msg = bot.send_message(chat_id, 'Чего изволите?', reply_markup=m.source_markup)

    elif message.text == "Погода🌤" or message.location is not None:
        if message.location is not None:
            observation = mgr.weather_at_coords(message.location.latitude, message.location.longitude)
            w = observation.weather
            temp = w.temperature('celsius')['temp']
            bot.send_message(message.chat.id, '🌤Cейчас ' + str(round(temp, 1)) + '°C')
        else:
            bot.send_message(message.chat.id, '🌤Вам необходимо выбрать локацию')

    elif message.text == "Гороскоп🔮":
        bot.send_message(message.chat.id,
                         text="Выберите ваш знак зодиака, чтобы получить гороскоп", reply_markup=im.inline_markup)

    elif message.text == "Курс валют💰":
        currencies = currency_parser.get_currency_exchange()
        text_to_send = ''

        for currency in currencies:
            text_to_send = text_to_send + f"Title: {currency.title}\nSell: {currency.sell}\nBuy: {currency.buy}\n\n"

        bot.send_message(message.chat.id, text=text_to_send)

    elif message.text == "Фильм🎬":
        film = cinema_parser.get_film()
        emoji_list = ['🎬', '🎨', '🎭', '🎥', '📽', '🎞']
        random_emoji = emoji_list[(random.randint(0, len(emoji_list) - 1))]
        message_back = f"{random_emoji} *{film.title}*, *{film.year}* \n *Жанр*: _{film.genre}_ \n\n {film.overview}"
        bot.send_message(message.chat.id, message_back, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    emoji_list = ['🪐', '💫', '⭐', '🌟', '✨', '⚡', '💥']
    random_emoji = emoji_list[(random.randint(0, len(emoji_list) - 1))]
    now = datetime.datetime
    for zodiak in zodiaks:
        if call.data == zodiak.short_name:
            horoscope_date = str(zodiak.telegram_bot_label) + ' на ' + str(now.today().strftime("%d.%m.%Y"))
            aries = open(f"horoscopes/{zodiak.title}_file.txt", 'r')
            answer = random_emoji + aries.readline()

    bot.send_message(call.message.chat.id, horoscope_date)
    bot.send_message(call.message.chat.id, answer)


x = threading.Thread(target=horoscope_parser.update_horoscopes_infinitelly)
x.start()

bot.polling()
