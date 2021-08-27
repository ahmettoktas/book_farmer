from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base import BaseFunctions
import time


# noinspection PyTypeChecker
class Functions(BaseFunctions):
    """
    Functions for blabla

    """

    PRODUCT_NAME_SELECTOR = (By.CLASS_NAME, "prd-name")
    PRODUCT_PRICE_SELECTOR = (By.CLASS_NAME, "prd-price")
    PRODUCT_PUBLISHER_SELECTOR = (By.CLASS_NAME, "prd-publisher")
    PRODUCT_ROW_SELECTOR = (By.CLASS_NAME, "prd-row")
    NEXT_PAGE_SELECTOR = (By.CSS_SELECTOR, ".icon.icon-next")
    PAGE_LEN_SELECTOR = (By.XPATH, "(//ul[@class = 'pager pager-list dr-flex pagination ']//li)[6]")
    BACK_BUTTON = (By.XPATH, '//li[@class = "mostMainCategory test1"]')
    PRODUCTS_NAME = {}
    PRODUCTS_PRICE = {}
    PRODUCT_PUBLISHER = {}
    PRODUCT_ROW = {}
    BOOK_INFO = ""
    txtDoc = ""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def collect_names(self):
        for z in range(15):
            self.click((By.CLASS_NAME, ('level' + str(z + 1))))
            if self.element_exists(self.NEXT_PAGE_SELECTOR) is False:
                self.click(self.BACK_BUTTON)
            else:
                for y in range(int(self.wait_for_element(self.PAGE_LEN_SELECTOR).text) - 1):
                    self.PRODUCTS_NAME = self.presence_for_elements(self.PRODUCT_NAME_SELECTOR)
                    self.PRODUCTS_PRICE = self.presence_for_elements(self.PRODUCT_PRICE_SELECTOR)
                    self.PRODUCT_PUBLISHER = self.presence_for_elements(self.PRODUCT_PUBLISHER_SELECTOR)
                    self.PRODUCT_ROW = self.presence_for_elements(self.PRODUCT_ROW_SELECTOR)
                    for x in range(len(self.PRODUCTS_NAME)):
                        self.BOOK_INFO = str(
                            self.PRODUCTS_NAME[x].text + " " + self.PRODUCTS_PRICE[x].text + " " +
                            self.PRODUCT_PUBLISHER[
                                x].text + " " + self.PRODUCT_ROW[x].text + "\n")
                        self.txtDoc = (self.txtDoc + self.BOOK_INFO)
                    self.scroll_specific_height(10000)
                    self.click(self.NEXT_PAGE_SELECTOR)
                    time.sleep(0.5)
                time.sleep(1)
                self.click(self.BACK_BUTTON)
        return self.txtDoc
