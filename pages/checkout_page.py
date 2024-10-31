from pages.base_page import BasePage
from utills.config import ConfigReader


class Checkout(BasePage):

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
