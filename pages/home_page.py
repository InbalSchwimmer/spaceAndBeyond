import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import HomePageLocators
from pages.locators import CheckoutPageLocators
from pages.base_page import BasePage
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.departure_date = None  # Initialize the departure date attribute

    def click_on_departure_picker(self):
        time.sleep(1)
        dates = self.driver.find_elements(*HomePageLocators.DEPARTURE_DATE_PICKER)
        dates[0].click()

    def click_on_returning_picker(self):
        time.sleep(1)
        dates = self.driver.find_elements(*HomePageLocators.DEPARTURE_DATE_PICKER)
        dates[1].click()

    def select_departure_date(self):
        time.sleep(1)
        # Add 2 months to the current date
        self.departure_date = datetime.now() + relativedelta(months=2)  # Store as datetime object
        target_day = self.departure_date.day
        target_year = self.departure_date.year

        while True:
            # Locate the month and year displayed in the calendar
            displayed_month_year = self.get_text(HomePageLocators.MONTH_YEAR_SELECTOR)
            displayed_month = displayed_month_year.split()[0]
            displayed_year = displayed_month_year.split()[1]

            # Check if the displayed month and year match the target month and year
            if int(displayed_year) == self.departure_date.year and displayed_month == self.departure_date.strftime(
                    "%B"):
                break
            else:
                # Click the next button to go to the next month
                self.click(HomePageLocators.DATE_PICKER_NEXT_BTN)
                time.sleep(1)  # Wait for the calendar to update

        # Click the target date in the calendar
        try:
            # Updated XPath to find the target date
            target_date_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, f"//div[@data-react-toolbox='day']/span[text()='{target_day}']"))
            )
            target_date_element.click()
        except Exception as e:
            print(f"Error selecting departure date: {e}")

    def select_returning_date(self):
        time.sleep(1)
        # Calculate the target date (1 week from departure date)
        target_date = self.departure_date + timedelta(weeks=1)  # This will now work
        target_day = target_date.day
        target_year = target_date.year

        while True:
            # Locate the month and year displayed in the calendar
            displayed_month_year = self.get_text(HomePageLocators.MONTH_YEAR_SELECTOR)
            displayed_month = displayed_month_year.split()[0]
            displayed_year = displayed_month_year.split()[1]

            # Check if the displayed month and year match the target month and year
            if int(displayed_year) == target_year and displayed_month == target_date.strftime("%B"):
                break
            else:
                # Click the next button to go to the next month
                self.click(HomePageLocators.DATE_PICKER_NEXT_BTN)
                time.sleep(1)  # Wait for the calendar to update

        # Click the target date in the calendar
        try:
            target_date_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[@data-react-toolbox='day']/span[text()='{target_day}']"))
            )
            target_date_element.click()
        except Exception as e:
            print(f"Error clicking the returning date: {e}")

    def get_selected_departure_date(self):
        try:
            # Locate the departure date input field using the updated selector
            departure_date_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(HomePageLocators.SELECTED_DEPARTURE_DATE)
            )
            # Retrieve and print the departure date value for debugging
            date_value = departure_date_element.get_attribute('value')
            print(f"Departure Date in Field: {date_value}")
            return date_value
        except Exception as e:
            print(f"Error retrieving selected departure date: {e}")

    def select_number_of_adults(self, value):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.ADULTS_DROPDOWN)
        )
        # Click the dropdown to display options
        self.click(HomePageLocators.ADULTS_DROPDOWN)

        # Wait until the options are visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.ADULTS_OPTIONS)
        )

        # Locate all the options in the dropdown specifically related to adults
        options = self.driver.find_elements(*HomePageLocators.ADULTS_OPTIONS)

        # Loop through the options and select the one that matches the value
        for option in options:
            if option.text == str(value):
                option.click()
                break
        else:
            print(f"Value '{value}' not found in the adults dropdown.")

    def select_number_of_children(self, value):

        # Click the dropdown to display options
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.CHILDREN_DROPDOWN)
        )
        self.click(HomePageLocators.CHILDREN_DROPDOWN)

        # Wait until the options are visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.CHILDREN_OPTIONS)
        )

        # Locate all the options in the dropdown specifically related to adults
        options = self.driver.find_elements(*HomePageLocators.CHILDREN_OPTIONS)

        # Loop through the options and select the one that matches the value
        for option in options:
            if option.text == str(value):
                option.click()
                break
        else:
            print(f"Value '{value}' not found in the children dropdown.")

    def select_planet_color(self, value):
        time.sleep(1)
        # Click the dropdown to display options
        self.click(HomePageLocators.PLANET_COLOR_DROPDOWN)

        # Wait until the options are visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.PLANET_COLOR_OPTION)
        )

        # Locate all the options in the dropdown specifically related to adults
        options = self.driver.find_elements(*HomePageLocators.PLANET_COLOR_OPTION)
        color_value = str(value).lower()
        # Loop through the options and select the one that matches the value
        for option in options:
            if option.text.lower() == value:
                time.sleep(1)
                option.click()
                break
        else:
            print(f"Value '{value}' not found in the planet color dropdown.")

    def slide_to_price(self, target_price):
        # Locate the progress bar element
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.PROGRESS_BAR)
        )
        progress_bar = self.driver.find_element(*HomePageLocators.PROGRESS_BAR)

        # Retrieve min, max, and width properties of the progress bar
        min_value = int(progress_bar.get_attribute("aria-valuemin"))
        max_value = int(progress_bar.get_attribute("aria-valuemax"))
        progress_bar_width = progress_bar.size['width']

        # Calculate the target position as a percentage of the bar width
        target_percentage = (target_price - min_value) / (max_value - min_value)
        target_pixel_position = int(progress_bar_width * target_percentage)

        # Calculate the exact movement in pixels relative to the current slider position
        action = ActionChains(self.driver)
        action.click_and_hold(progress_bar).move_by_offset(-progress_bar_width // 2, 0)  # Start from minimum
        action.move_by_offset(target_pixel_position, 0).release().perform()  # Move to target position

    def scroll_to_element_and_click(self, element):
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the button to be present in the DOM
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(element)  # Locate the element in the DOM
        )

        # Scroll to the element using JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", button)

        # Optional: Wait a moment for the scrolling to finish
        time.sleep(0.5)

        # Check if the button is clickable after scrolling
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button)  # Confirm it can be clicked
        )

        # Click the button
        button.click()

    def fill_travel_data(self, adults, children, color, price, destination):
        with allure.step("Select number of adults"):
            self.select_number_of_adults(adults)
        with allure.step("Select number of children"):
            self.select_number_of_children(children)
        with allure.step("Select planet color of adults"):
            self.select_planet_color(color)
        with allure.step("Select price"):
            self.slide_to_price(price)
        with allure.step("Select destination"):
            self.scroll_to_element_and_click(destination)

