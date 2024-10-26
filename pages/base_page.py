import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            return self.driver.find_element(*locator).text
        except NoSuchElementException:
            return False

    def fill_text(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element(locator)
            )
            self.driver.find_element(*locator).clear()
        except NoSuchElementException:
            print("Element not exist")
        self.driver.find_element(*locator).send_keys(text)

    def element_exist(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_current_url(self):
        current_url = self.driver.current_url
        return  current_url

    def scroll_to_page_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

