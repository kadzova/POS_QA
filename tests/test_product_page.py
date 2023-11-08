from pages.product_page import ProductPage
from data.data_urls import PRODUCT_PAGE_URL, CHECKOUT_PAGE_URL


class TestProductPage:

    def test_adding_a_multiple_quantities_of_the_product_to_the_cart(self, driver):
        """
        Checks if the product is added to the cart successfully with a quantity between 5 and 10.
        """
        product_page = ProductPage(driver, PRODUCT_PAGE_URL)
        product_page.open()
        product_page.check_size_32_and_color_blue()
        product_page.fill_in_quantity_field()
        displayed_quantity = product_page.get_quantity_field_attribute("value")
        assert 5 <= int(displayed_quantity) <= 10, "Displayed quantity isn't within the expected range (5-10)"
        assert product_page.message_text() == 'You added Lono Yoga Short to your shopping cart.', \
            'The message is incorrect'

    def test_proceed_to_checkout_button_redirects_to_checkout_page(self, driver):
        """
        Checks if clicking on the "Proceed to Checkout" button redirects to the checkout page.
        """
        product_page = ProductPage(driver, PRODUCT_PAGE_URL)
        product_page.open()
        product_page.check_size_32_and_color_blue()
        product_page.fill_in_quantity_field()
        product_page.proceed_to_checkout()
        assert product_page.get_actual_url_of_current_page() == CHECKOUT_PAGE_URL
