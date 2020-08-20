from selenium import webdriver
from zodiak import Zodiak
import time
import datetime

zodiaks = [
    Zodiak('aries', '🔮♈ Гороскоп для Овнов', 'Овен'),
    Zodiak('gemini', '🔮♊ Гороскоп для Близнецов', 'Близнецы'),
    Zodiak('taurus', '🔮♉ Гороскоп для Тельцов', 'Телец'),
    Zodiak('cancer', '🔮♋ Гороскоп для Раков', 'Рак'),
    Zodiak('leo', '🔮♌ Гороскоп для Львов', 'Лев'),
    Zodiak('virgo', '🔮♍ Гороскоп для Дев', 'Дева'),
    Zodiak('libra', '🔮♎ Гороскоп для Весов', 'Весы'),
    Zodiak('scorpio', '🔮♏ Гороскоп для Скорпионов', 'Скорпион'),
    Zodiak('sagittarius', '🔮♐ Гороскоп для Стрельцов', 'Стрелец'),
    Zodiak('capricorn', '🔮♑ Гороскоп для Козерогов', 'Козерог'),
    Zodiak('aquarius', '🔮♒ Гороскоп для Водолеев', 'Водолей'),
    Zodiak('pisces', '🔮♓ Гороскоп для Рыб', 'Рыбы')
]


class HoroscopeParser:
    def update_horoscopes(self):
        driver = webdriver.Chrome()
        for zodiak in zodiaks:
            self.update_horoscope(driver, zodiak.title)
        driver.close()

    def update_horoscope(self, driver, zodiak):
        try:
            driver.get(f"https://goroskop.i.ua/{zodiak}/c/")
            zodiak_file = open(f"horoscopes/{zodiak}_file.txt", 'w')
            element = driver.find_element_by_tag_name("p").text
            zodiak_file.write(element)
            zodiak_file.close()
        except Exception as e:
            print('[log] Error')

    def update_horoscopes_infinitelly(self):
        self.update_horoscopes()
        while True:
            time.sleep(30)
            if datetime.datetime.now().minute == 00:
                self.update_horoscopes()
