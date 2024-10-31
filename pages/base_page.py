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
        self.wait_for_clickable(locator)
        return self.driver.find_element(*locator).text

    def fill_text(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element(locator)
            )
            self.driver.find_element(*locator).clear()
        except NoSuchElementException:
            print("Element not exist")
        self.driver.find_element(*locator).send_keys(text)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def scroll_to_page_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_clickable(self, locator, return_element=False, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            if return_element:
                return self.driver.find_element(*locator)
        except NoSuchElementException:
            print(f"Element {locator} not found.")

    def wait_for_element_visibility(self, locator, return_element=False, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)

            )
            if return_element:
                return self.driver.find_element(*locator)
        except NoSuchElementException:
            print("Element not exist")

    def wait_for_all_element_visibility(self, locator, return_element=False, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            if return_element:
                return self.driver.find_elements(*locator)
        except NoSuchElementException:
            print("Element not exist")
