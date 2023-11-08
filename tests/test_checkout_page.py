import time

import pytest

from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from data.data_urls import PRODUCT_PAGE_URL, CHECKOUT_PAGE_URL


@pytest.fixture(scope='function')
def get_into_checkout_page(driver):
    page = ProductPage(driver, PRODUCT_PAGE_URL)
    page.open()
    page.check_size_32_and_color_blue()
    page.fill_in_quantity_field()
    page.proceed_to_checkout()


class TestCheckoutPage:
    def test_fill_checkout_fields(self, driver, get_into_checkout_page):
        """
        This test is designed to fill in the checkout fields with credentials, select a state from the dropdown,
        select a radio button, click the next button, click the place order button,
        and then assert if the success message is as expected.
        """
        checkout_page = CheckoutPage(driver, CHECKOUT_PAGE_URL)
        checkout_page.open()
        checkout_page.fill_the_fields_with_credentials()
        checkout_page.dropdown_state()
        checkout_page.select_radio_button()
        checkout_page.click_next_button()
        time.sleep(5)
        checkout_page.click_place_order()
        time.sleep(5)
        assert checkout_page.message_text() == "Thank you for your purchase!"
