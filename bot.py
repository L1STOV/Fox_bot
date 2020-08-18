import telebot
import config
import pyowm
import markup as m
import inline_markup as im

city = 'Николаев, Украина'  # need to create func that will detect location
owm_api_key = config.owm_api_token
owm = pyowm.OWM(owm_api_key)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temp = w.temperature('celsius')['temp']

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


bot.polling()
