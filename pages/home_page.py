from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    DEPARTURE_DATE_PICKER = (By.XPATH, "//label[@class = 'theme__label___tqKDt' and text() = 'Departing']")
    RETURNING_DATE_PICKER = (By.XPATH, "//label[text() = 'Returning']")
    MONTH_YEAR_SELECTOR = (By.XPATH, "//span[@class='theme__title___2Ue3-']")

    def __init__(self, driver):
        super().__init__(driver)

    # def select_departure_date(self):
    #     target_date = datetime.now() + timedelta(weeks=2)
    #     target_day = target_date.day
    #     target_month = target_date.month
    #     target_year = target_date.year
    #
    #     while True:
    #         # Locate the month and year displayed in the calendar
    #         displayed_month_year = self.get_text(MONTH_YEAR_SELECTOR)
    #         displayed_month = displayed_month_year.split()[0]
    #         displayed_year = displayed_month_year.split()[1]
    #
    #         # Check if the displayed month and year match the target month and year
    #         if int(displayed_year) == target_year and displayed_month == target_date.strftime("%B"):
    #             break
    #         else:
    #             # Click the next button to go to the next month
    #             next_button = driver.find_element(By.CLASS_NAME, "datepicker-next")
    #             next_button.click()
    #             time.sleep(1)  # Wait for the calendar to update
    #
    #     # Step 6: Click the target date in the calendar
    #     target_date_element = driver.find_element(By.XPATH, f"//td[text()='{target_day}']")
    #     target_date_element.click()
