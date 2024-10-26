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
    @allure.description("This test verifies that click on book a flight button after filling in the flight details "
                        "will display checkout section by verifying url")
    @allure.title("Verify flight booking redirects to checkout")
    def test_num_of_travelers(self):
        user = Checkout(self.driver)
        flight = HomePage(self.driver)
        with allure.step("Select destination"):
            flight.scroll_to_element_and_click(HomePage.BOOK_BABAHOYO_BTN)
        user.fill_text(user.NAME_TEXT_FILED, "Inbal")
        time.sleep(10)
