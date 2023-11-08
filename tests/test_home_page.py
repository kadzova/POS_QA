from pages.home_page import HomePage
from data.data_urls import MAIN_PAGE_URL, MEN_SUBSECTION_SHORTS_PAGE, PRODUCT_PAGE_URL


class TestHomePage:

    def test_mens_subsection_shorts_link(self, driver):
        """
        Checks if clicking on the "Shorts" link in the "Men" section redirects to
        the Shorts page and if the header is displayed correctly.
        """
        home_page = HomePage(driver, MAIN_PAGE_URL)
        home_page.open()
        home_page.check_men_shorts_subsection_link()
        assert home_page.get_actual_url_of_current_page() == MEN_SUBSECTION_SHORTS_PAGE, \
            "Shorts page of Men section is either not opened or the page header is incorrect"

    def test_filter_category(self, driver):
        """
        Checks if the filters (Style-Compression, Material-Polyester, New-Yes)
        are set correctly after applying the filter block.
            """
        home_page = HomePage(driver, MEN_SUBSECTION_SHORTS_PAGE)
        home_page.open()
        home_page.check_filter_block()
        assert home_page.filter_current_style_text() == 'Compression' and \
               home_page.filter_current_material_text() == 'Polyester' \
               and home_page.filter_current_new_text() == 'Yes', "Expected values 'Compression', 'Polyester', 'No'" \
                                                                 " are not accurate"

    def test_product_page_is_open(self, driver):
        """
        Checks if the product page opens correctly after applying the filter block.
        """
        home_page = HomePage(driver, MEN_SUBSECTION_SHORTS_PAGE)
        home_page.open()
        home_page.check_filter_block()
        home_page.open_product_page()
        assert home_page.get_actual_url_of_current_page() == PRODUCT_PAGE_URL
