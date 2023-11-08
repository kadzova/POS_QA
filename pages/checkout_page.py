import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.locators import CheckoutPageLocators
from data.data_credentials_for_checkout import CredentialsForCheckout


class CheckoutPage(BasePage):
    checkout_locators = CheckoutPageLocators
    credentials = CredentialsForCheckout

    def fill_the_fields_with_credentials(self):
        """
        Fills in various fields (Email, First Name, Last Name, Street Address, City, Zip/Postal Code, Phone Number)
        with the provided credentials.
        """
        # Email
        email_field = self.element_is_clickable(self.checkout_locators.EMAIL_FIELD)
        email_field.click()
        email_field.clear()
        email_credentials = self.credentials.email
        email_field.send_keys(email_credentials)

        # First Name
        first_name_field = self.element_is_clickable(self.checkout_locators.FIRST_NAME_FIELD)
        first_name_field.click()
        first_name_field.clear()
        first_name_credentials = self.credentials.first_name
        first_name_field.send_keys(first_name_credentials)

        # Last Name
        last_name_field = self.element_is_clickable(self.checkout_locators.LAST_NAME_FIELD)
        last_name_field.click()
        last_name_field.clear()
        last_name_credentials = self.credentials.last_name
        last_name_field.send_keys(last_name_credentials)

        # Street Address
        street_address_field = self.element_is_clickable(self.checkout_locators.STREET_ADDRESS_FIELD)
        street_address_field.click()
        street_address_field.clear()
        street_address_credentials = self.credentials.street_address
        street_address_field.send_keys(street_address_credentials)

        # City
        city_field = self.element_is_clickable(self.checkout_locators.CITY_FIELD)
        city_field.click()
        city_field.clear()
        city_credentials = self.credentials.city
        city_field.send_keys(city_credentials)

        # Zip/Postal Code
        zip_code_field = self.element_is_clickable(self.checkout_locators.ZIP_CODE_FIELD)
        zip_code_field.click()
        zip_code_field.clear()
        zip_code_credentials = self.credentials.zip_code
        zip_code_field.send_keys(zip_code_credentials)

        # Phone Number
        phone_number_field = self.element_is_clickable(self.checkout_locators.PHONE_NUMBER_FIELD)
        phone_number_field.click()
        phone_number_field.clear()
        phone_number_credentials = self.credentials.phone_number
        phone_number_field.send_keys(phone_number_credentials)
        return

    def dropdown_state(self):
        """
        Selects the state from a dropdown menu.
        """
        self.select_option_from_dropdown(self.checkout_locators.STATE_DROP_DOWN, 'California')
        return

    def select_radio_button(self):
        """
        Selects a radio button.
        """
        radio_button_locator = self.checkout_locators.RADIO_BUTTON
        radio_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(radio_button_locator))
        radio_button.click()

    def click_next_button(self):
        """
        Clicks the "Next" button to proceed to next step.
        """
        return self.click(self.checkout_locators.NEXT_BUTTON)

    def click_place_order(self):
        """
        Clicks the "Place Order" button to finish checkout.
        """
        return self.click(self.checkout_locators.PLACE_ORDER_BUTTON)

    def message_text(self):
        """
        Gets the text of a message (e.g., success message).
        """
        return self.get_text(self.checkout_locators.SUCCESS_MESSAGE)
