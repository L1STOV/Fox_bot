import telebot
import config
import datetime
import random
import pyowm
import requests
import markup as m
import inline_markup as im
from selenium import webdriver


# Weather
city = 'Николаев, Украина'  # need to create func that will detect location
owm_api_key = config.owm_api_token
owm = pyowm.OWM(owm_api_key)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temp = w.temperature('celsius')['temp']

# Variable for data and time
now = datetime.datetime.now()

# Bot init
bot = telebot.TeleBot(config.tel_api_token)


@bot.message_handler()
def fox_init(message):

    if message.text == "/start":
        chat_id = message.chat.id
        intro_msg = f"Привет , {message.from_user.first_name}👋🏻" \
                    "\nМеня зовут Фокс🦊 и я твой персональный помощник☺"
        msg = bot.send_message(message.chat.id, intro_msg)
        msg = bot.send_message(chat_id, 'Чего изволите?', reply_markup=m.source_markup)

    elif message.text == "Погода🌤":
        bot.send_message(message.chat.id, '🌤В городе ' + city + ' сейчас ' + str(round(temp, 1)) + '°C')

    elif message.text == "Гороскоп🔮":
        bot.send_message(message.chat.id,
                         text="Выберите ваш знак зодиака, чтобы получить гороскоп", reply_markup=im.inline_markup)

        @bot.callback_query_handler(func=lambda call: True)
        # All about horoscope
        def query_handler(call):
            horoscope = ''
            emoji_list = ['🪐', '💫', '⭐', '🌟', '✨', '⚡', '💥']
            random_emoji = emoji_list[(random.randint(0, len(emoji_list)))]
            driver = webdriver.Chrome()
            if call.data == 'Овен':
                horoscope_date = '🔮♈ Гороскоп для Овнов на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/aries/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Близнецы':
                horoscope_date = '🔮♊ Гороскоп для Близнецов на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/gemini/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Телец':
                horoscope_date = '🔮♉ Гороскоп для Тельцов на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/taurus/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Рак':
                horoscope_date = '🔮♋ Гороскоп для Раков на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/cancer/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Лев':
                horoscope_date = '🔮♌ Гороскоп для Львов на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/leo/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Дева':
                horoscope_date = '🔮♍ Гороскоп для Дев на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/virgo/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Весы':
                horoscope_date = '🔮♎ Гороскоп для Весов на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/libra/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Скорпион':
                driver.get("https://goroskop.i.ua/scorpio/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Стрелец':
                horoscope_date = '🔮♐ Гороскоп для Стрельцов на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/sagittarius/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Козерог':
                horoscope_date = '🔮♑ Гороскоп для Козерогов на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/capricorn/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Водолей':
                horoscope_date = '🔮♒ Гороскоп для Водолеев на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/aquarius/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text
            if call.data == 'Рыбы':
                horoscope_date = '🔮♓ Гороскоп для Рыб на ' + str(now.day) + '.' + str(now.strftime("%m"))
                driver.get("https://goroskop.i.ua/pisces/c/")
                answer = str(random_emoji) + driver.find_element_by_tag_name("p").text

            bot.send_message(call.message.chat.id, horoscope_date)
            bot.send_message(message.chat.id, answer)


bot.polling()
