import time

import allure
import pytest
from allure_commons.types import Severity

from pages.checkout_page import Checkout
from pages.home_page import HomePage


class TestCheckout:
    @pytest.mark.functional
    @pytest.mark.regression
    @allure.severity(Severity.BLOCKER)
    @allure.description("This test verifies that numbers of travelers that was booked to the flight display in "
                        "checkout section")
    @allure.title("Verify numbers of travelers in checkout")
    def test_num_of_travelers(self):
        book_flight = HomePage(self.driver)
        with allure.step("Select departure date"):
            book_flight.click_on_departure_picker()
            book_flight.select_departure_date()
            book_flight.click(HomePage.CALENDER_OK_BTN)
        with allure.step("Select returning date"):
            book_flight.click_on_returning_picker()
            book_flight.select_returning_date()
            book_flight.click(HomePage.CALENDER_OK_BTN)
        with allure.step("Check the order price"):
            book_flight.fill_travel_data(3, 2, "blue", 1000, HomePage.BOOK_BABAHOYO_BTN)
        with allure.step("Assert number of travelers as was entered"):
            user = Checkout(self.driver)
            num_of_travelers = user.get_text(user.NUMBER_OF_TRAVELERS)
            assert num_of_travelers == "5 travelers"

    @pytest.mark.regression
    @allure.severity(Severity.BLOCKER)
    @allure.description("This test verifies that the total price of the order is as expected by calculating ticket "
                        "price * number of travelers")
    @allure.title("Verify order price as expected")
    def test_total_order_price(self):
        book_flight = HomePage(self.driver)
        with allure.step("Select departure date"):
            book_flight.click_on_departure_picker()
            book_flight.select_departure_date()
            book_flight.click(HomePage.CALENDER_OK_BTN)
        with allure.step("Select returning date"):
            book_flight.click_on_returning_picker()
            book_flight.select_returning_date()
            book_flight.click(HomePage.CALENDER_OK_BTN)
        with allure.step("Fill order details"):
            book_flight.fill_travel_data(3, 2, "blue", 1000, HomePage.BOOK_BABAHOYO_BTN)
        with allure.step("Check the order price"):
            user = Checkout(self.driver)
            expected_price = user.calculate_price_order(5, "babahoyo")
            order_price = user.get_text(user.ORDER_TOTAL_SUM)
            actual_price = user.price_without_signs(order_price)
        with allure.step("Assert actual_price is equal to expected_price"):
            assert actual_price == expected_price
