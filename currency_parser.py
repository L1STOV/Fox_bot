from selenium import webdriver
from currency import Currency
import time
import datetime


class CurrencyParser:

    def get_currency_exchange(self):
        driver = webdriver.Chrome()
        driver.get("https://finance.i.ua/")
        time.sleep(2)

        usd_row = driver.find_element_by_css_selector(".widget-currency_summary table > tbody > tr:nth-child(1)")
        eur_row = driver.find_element_by_css_selector(".widget-currency_summary table > tbody > tr:nth-child(2)")
        rub_row = driver.find_element_by_css_selector(".widget-currency_summary table > tbody > tr:nth-child(3)")
        pln_row = driver.find_element_by_css_selector(".widget-currency_summary table > tbody > tr:nth-child(4)")

        rub_currency = self.parse_currency(rub_row)
        usd_currency = self.parse_currency(usd_row)
        eur_currency = self.parse_currency(eur_row)
        pln_currency = self.parse_currency(pln_row)

        driver.close()
        return [usd_currency, eur_currency, rub_currency, pln_currency]

    def parse_currency(self, row_element_by_css_selector):

        currency = Currency()
        currency.title = row_element_by_css_selector.find_element_by_css_selector('th').text
        currency.sell = row_element_by_css_selector.find_element_by_css_selector('td:nth-child(2) span > span').text
        currency.buy = row_element_by_css_selector.find_element_by_css_selector('td:nth-child(3) span > span').text

        return currency


