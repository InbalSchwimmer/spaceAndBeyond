from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utills.config import ConfigReader


class Checkout(BasePage):
    NAME_TEXT_FILED = (By.XPATH, "//div[@data-react-toolbox='input']//span[text()='Name']/preceding-sibling::input")
    NUMBER_OF_TRAVELERS = (By.XPATH, "//div[@class ='flexboxgrid__col-xs-7___3o2m-' and contains(text(), 'travelers')]")
    ORDER_TOTAL_SUM = (By.CSS_SELECTOR, ".OrderSummary__headline-1___1lzsL")

    def __init__(self, driver):
        super().__init__(driver)

    def calculate_price_order(self, num_of_travelers, destination):
        dest = destination.lower()
        price_of_one_ticket = float(ConfigReader.read_config("tickets_price", dest))
        total = num_of_travelers * price_of_one_ticket
        return total

    def price_without_signs(self, price):
        # Remove the dollar sign and commas, then convert to float
        clean_price = float(price.replace('$', '').replace(',', ''))
        return clean_price
