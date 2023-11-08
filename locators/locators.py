"""This section contains locators"""

from selenium.webdriver.common.by import By


class HomePageLocators:
    MEN_SECTION = By.XPATH, '//*[@id="ui-id-5"]'
    BOTTOMS_SUBSECTION = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]'
    PANTS = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]/ul/li[1]'
    SHORTS = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]/ul/li[2]'


class FilterLocators:
    STYLE_CATEGORY = By.XPATH, '//*[@id="narrow-by-list"]/div[1]'
    STYLE_CATEGORY_COMPRESSION = By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[2]/ol/li[2]/a'
    MATERIAL_CATEGORY = By.XPATH, '//*[@id="narrow-by-list"]/div[4]'
    MATERIAL_CATEGORY_POLYESTER = By.XPATH, '//*[@id="narrow-by-list"]/div[4]/div[2]/ol/li[5]/a'
    NEW_CATEGORY = By.XPATH, '//*[@id="narrow-by-list"]/div[6]'
    NEW_CATEGORY_YES = By.XPATH, '//*[@id="narrow-by-list"]/div[6]/div[2]/ol/li[1]/a'


class FilterCurrent:
    STYLE = By.XPATH, '//div[@class="filter-current"]/ol/li[1]/span[2]'
    MATERIAL = By.XPATH, '//div[@class="filter-current"]/ol/li[2]/span[2]'
    NEW = By.XPATH, '//div[@class="filter-current"]/ol/li[3]/span[2]'
    PRODUCT = By.CSS_SELECTOR, '.product-item-info'


class ProductPageLocators:
    SIZE_32 = By.CSS_SELECTOR, '#option-label-size-143-item-175'
    COLOR_BLUE = By.CSS_SELECTOR, '#option-label-color-93-item-50'
    QTY_INPUT = By.CSS_SELECTOR, '#qty'
    QUANTITY_NUMBER = By.CSS_SELECTOR, 'input.input-text.qty'
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, '#product-addtocart-button'
    MESSAGE = By.XPATH, '//*[@role="alert"]/div/div'
    CART = By.CSS_SELECTOR, '.minicart-wrapper>a'
    PROCEED_TO_CHECKOUT_BUTTON = By.CSS_SELECTOR, '#top-cart-btn-checkout'
    SHIPPING_TITLE = By.CSS_SELECTOR, '#shipping > div.step-title'


class CheckoutPageLocators:

    """ID's elements are dynamic(random numbers), don't use Xpath/CSS locators by ID"""

    EMAIL_FIELD = By.XPATH, '//*[@id="customer-email"]'
    FIRST_NAME_FIELD = By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[1]/div/input'
    LAST_NAME_FIELD = By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[2]/div/input'
    STREET_ADDRESS_FIELD = By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/fieldset/div/div[1]/div/input'
    CITY_FIELD = By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[4]/div/input'
    STATE_DROP_DOWN = By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[5]/div/select'
    ZIP_CODE_FIELD = By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[7]/div/input'
    COUNTRY_DROP_DOWN = By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[8]/div/select'
    PHONE_NUMBER_FIELD = By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form[2]/div/div[9]/div/input'
    RADIO_BUTTON = By.CSS_SELECTOR, 'input[type="radio"]'
    NEXT_BUTTON = By.CSS_SELECTOR, '.button'
    PLACE_ORDER_BUTTON = By.XPATH, '//*[@class="action primary checkout"]'
    SUCCESS_MESSAGE = By.XPATH, '//*[@class="base"]'

