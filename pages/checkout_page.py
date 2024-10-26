from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Checkout(BasePage):
    NAME_TEXT_FILED = (By.XPATH, "//div[@data-react-toolbox='input']//span[text()='Name']/preceding-sibling::input")
    NUMBER_OF_TRAVELERS = (By.CSS_SELECTOR, ".OrderSummary__row-3___1s0Ls.flexboxgrid__row___1y_mg")

    def __init__(self, driver):
        super().__init__(driver)

