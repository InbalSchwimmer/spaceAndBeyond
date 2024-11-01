import time
import allure
import pytest
from allure_commons.types import Severity
from pages.home_page import HomePage
from utills.config import ConfigReader
from pages.locators import HomePageLocators


class TestBookingFlight:

    @pytest.mark.functional
    @pytest.mark.regression
    @allure.severity(Severity.BLOCKER)
    @allure.description("This test verifies that click on book a flight button after filling in the flight details "
                        "will navigates to checkout page "
                        "section by verifying url")
    @allure.title("Verify flight booking redirects to checkout")
    def test_booking_flight(self):
        book_flight = HomePage(self.driver)
        with allure.step("Select departure date"):
            book_flight.click_on_departure_picker()
            book_flight.select_departure_date()
            book_flight.click(HomePageLocators.CALENDER_OK_BTN)
        with allure.step("Select returning date"):
            book_flight.click_on_returning_picker()
            book_flight.select_returning_date()
            book_flight.click(HomePageLocators.CALENDER_OK_BTN)
        book_flight.fill_travel_data(3, 2, "blue", 1000, HomePageLocators.BOOK_BABAHOYO_BTN)
        with allure.step("Assert url change to checkout url"):
            current_url = book_flight.get_current_url()
            expected_url = ConfigReader.read_config("general", "checkout_url")
            assert current_url == expected_url

    @pytest.mark.regression
    @allure.severity(Severity.NORMAL)
    @allure.description("This test verifies that departure date display as was entered")
    @allure.title("Verify departure date display as set")
    def test_departure_date(self):
        book_flight = HomePage(self.driver)
        with allure.step("Select departure date"):
            book_flight.click_on_departure_picker()
            book_flight.select_departure_date()
            book_flight.click(HomePageLocators.CALENDER_OK_BTN)
        with allure.step("Assert selected departure date as requested"):
            displayed_departure_date = book_flight.get_selected_departure_date()
            # Convert book_flight.departure_date to string
            expected_date = book_flight.change_format_date(book_flight.departure_date)
            assert displayed_departure_date == expected_date

    @pytest.mark.regression
    @allure.severity(Severity.NORMAL)
    @allure.description("This test verifies that click on 'select destination' button will navigates to select  "
                        "destination selection page")
    @allure.title("Verify 'Select Destination' button navigates to the destination selection page")
    def test_destination_btn(self):
        book_flight = HomePage(self.driver)
        with allure.step("Select departure date"):
            book_flight.click_on_departure_picker()
            book_flight.select_departure_date()
            book_flight.click(HomePageLocators.CALENDER_OK_BTN)
        with allure.step("Assert click on destination btn will display destination url"):
            book_flight.click(HomePageLocators.SELECT_DESTINATION_BTN)
            current_url = book_flight.get_current_url()
            expected_url = ConfigReader.read_config("general", "destinations_url")
            assert current_url == expected_url
