import time

from pages.home_page import HomePage


class TestBookingFlight:

    def test_booking_flight(self):
        book_flight = HomePage(self.driver)
        book_flight.click(HomePage.DEPARTURE_DATE_PICKER)

