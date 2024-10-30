# locators.py
from selenium.webdriver.common.by import By


class HomePageLocators:
    DEPARTURE_DATE_PICKER = (By.CSS_SELECTOR, "[data-react-toolbox='date-picker']")
    RETURNING_DATE_PICKER = (By.XPATH, "//label[text() = 'Returning']")
    MONTH_YEAR_SELECTOR = (By.XPATH, "//span[@class='theme__title___2Ue3-']")
    CALENDER_OK_BTN = (By.XPATH, "//button[text()='Ok']")
    DATE_PICKER_NEXT_BTN = (By.CSS_SELECTOR, "#right")
    SELECTED_DEPARTURE_DATE = (By.CSS_SELECTOR, "div[data-react-toolbox='date-picker']:nth-of-type(1) input["
                                                "type='text']")
    ADULTS_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'WhiteDropDown__dropdown')])[1]")
    ADULTS_OPTIONS = (By.XPATH, "//ul[contains(@class, 'WhiteDropDown__values___3lOeL') and contains(., 'Adults')]//li")
    CHILDREN_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'WhiteDropDown__dropdown')])[2]")
    CHILDREN_OPTIONS = (By.XPATH, "//ul[contains(@class, 'WhiteDropDown__values___3lOeL') and contains(., "
                                  "'Children')]//li")
    PLANET_COLOR_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'Gallery__dropdown-size-1___3IWmB')])[2]")
    PLANET_COLOR_OPTION = (By.XPATH, "//ul[contains(@class, 'theme__values___1jS4g') and .//li[text()='Planet "
                                     "color']]//li")
    PROGRESS_BAR = (By.CSS_SELECTOR, "[data-react-toolbox='progress-bar']")
    BOOK_BABAHOYO_BTN = (By.CSS_SELECTOR, " div > div:nth-child(3) > div button")
    SELECT_DESTINATION_BTN = (By.CSS_SELECTOR, ".Hero__cta-button___9VskW")


class CheckoutPageLocators:
    NAME_TEXT_FILED = (By.XPATH, "//div[@data-react-toolbox='input']//span[text()='Name']/preceding-sibling::input")
    NUMBER_OF_TRAVELERS = (By.XPATH, "//div[@class ='flexboxgrid__col-xs-7___3o2m-' and contains(text(), 'travelers')]")
    ORDER_TOTAL_SUM = (By.CSS_SELECTOR, ".OrderSummary__headline-1___1lzsL")
