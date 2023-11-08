from pages.base_page import BasePage
from locators.locators import ProductPageLocators
import random


class ProductPage(BasePage):
    product_locators = ProductPageLocators

    def check_size_32_and_color_blue(self):
        """
        This method checks size 32 and color blue
        """
        self.click(self.product_locators.SIZE_32)
        self.click(self.product_locators.COLOR_BLUE)
        return

    def random_qty(self):
        """
        This method generate a random number between 5 and 10
        """
        random_num = random.randint(5, 10)
        return random_num

    def fill_in_quantity_field(self):
        """
        This method fills in quantity input field with a random quantity and adds the product to the cart.
        """
        input_field = self.element_is_clickable(self.product_locators.QTY_INPUT)
        input_field.click()
        input_field.clear()
        qty = self.random_qty()
        input_field.send_keys(qty)
        self.click(self.product_locators.ADD_TO_CART_BUTTON)
        # time.sleep(5)
        return

    def get_quantity_field_attribute(self, attribute):
        """
        This method gets a specified attribute of the quantity field
        """
        quantity_input = self.element_is_clickable(self.product_locators.QUANTITY_NUMBER)
        return quantity_input.get_attribute(attribute)

    def go_to_shopping_cart(self):
        """
        Navigates to the shopping cart page.
        """
        return self.click(self.product_locators.CART)

    def message_text(self):
        """
        Retrieves the text of a message (e.g., success message).
        """
        return self.get_text(self.product_locators.MESSAGE)

    def proceed_to_checkout(self):
        """
        Proceeds to the checkout process by clicking the "Proceed to Checkout" button.
        """
        self.wait_for_element_to_load(self.product_locators.MESSAGE)
        self.click(self.product_locators.CART)
        self.click(self.product_locators.PROCEED_TO_CHECKOUT_BUTTON)
        self.wait_for_element_to_load(self.product_locators.SHIPPING_TITLE)
        return
