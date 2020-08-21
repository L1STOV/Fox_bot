from selenium import webdriver
import time
from cinema import Cinema


class CinemaParser:
    def get_film(self):
        cinema = Cinema()
        driver = webdriver.Chrome()
        driver.get("https://generator-online.com/movies/")
        time.sleep(1)
        btn_element = driver.find_element_by_css_selector("button[class^='btn-floating'] span").click()
        time.sleep(1)
        cinema.title = driver.find_element_by_id('title').text
        cinema.genre = driver.find_element_by_id('genres').text
        cinema.year = driver.find_element_by_id('release_date').text
        cinema.overview = driver.find_element_by_id('overview').text
        driver.close()
        return cinema
