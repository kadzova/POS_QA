from pages.base_page import BasePage
from locators.locators import HomePageLocators, FilterLocators, FilterCurrent


class HomePage(BasePage):
    homepage_locators = HomePageLocators
    filter_locators = FilterLocators
    current_filter = FilterCurrent

    'Check the "Shorts" link of the "Men" section'
    def check_men_shorts_subsection_link(self):
        """
        Verifies that the "Shorts" link of the "Men" section is visible and interactive.
        """
        self.action_move_to_element(self.element_is_visible(self.homepage_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.homepage_locators.BOTTOMS_SUBSECTION))
        self.action_move_to_element(self.element_is_visible(self.homepage_locators.PANTS))
        self.click(self.homepage_locators.SHORTS)
        return

    def check_filter_block(self):
        """
        Verifies that the filter categories are set to Style-Compression, Material-Polyester, New-Yes.
        """
        self.click(self.filter_locators.STYLE_CATEGORY)
        self.click(self.filter_locators.STYLE_CATEGORY_COMPRESSION)
        self.click(self.filter_locators.MATERIAL_CATEGORY)
        self.click(self.filter_locators.MATERIAL_CATEGORY_POLYESTER)
        self.click(self.filter_locators.NEW_CATEGORY)
        self.click(self.filter_locators.NEW_CATEGORY_YES)
        return

    def filter_current_style_text(self):
        """
        Gets the text of the current style filter.
        :return: text
        """
        return self.get_text(self.current_filter.STYLE)

    def filter_current_material_text(self):
        """
        Gets the text of the current material filter.
        :return: text
        """
        return self.get_text(self.current_filter.MATERIAL)

    def filter_current_new_text(self):
        """
        Gets the text of the current new filter.
        :return:
        """
        return self.get_text(self.current_filter.NEW)

    def open_product_page(self):
        """
        Clicks on a product link to navigate to the product page.
        """
        self.click(self.current_filter.PRODUCT)
        return


