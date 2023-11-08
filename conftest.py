import pytest
from selenium import webdriver
from pages.home_page import HomePage
from data.data_urls import MAIN_PAGE_URL


@pytest.fixture(scope="function")
def driver():
    """ This fixture sets up a Chrome WebDriver instance before each test that uses it,
    and it ensures that the WebDriver is properly cleaned up after the test finishes."""
    driver = webdriver.Chrome()
    driver.set_window_size(1900, 1000)
    driver.maximize_window()
    yield driver
    driver.quit()



# @pytest.fixture(scope="function")
# def home_page(driver):
#     """This fixture navigates to Home page and opens it for testing"""
#     home_page = HomePage(driver, MAIN_PAGE_URL)
#     home_page.open()
#     return home_page

