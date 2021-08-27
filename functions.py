from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base import BaseFunctions
import time


class Functions(BaseFunctions):
    """
    Functions for blabla

    """

    PRODUCT_NAME_SELECTOR = (By.CLASS_NAME, "prd-name")
    PRODUCT_PRICE_SELECTOR = (By.CLASS_NAME, "prd-price")
    BOOK_INFO = ""
    PRODUCTS_NAME = {}
    PRODUCTS_PRICE = {}
    TXTDOC = ""
    NEXT_PAGE = (By.CSS_SELECTOR, ".icon.icon-next")
    PAGE_LENGHT = (By.XPATH, "(//ul[@class = 'pager pager-list dr-flex pagination ']//li)[6]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 90)

    def collect_names(self):
        for b in range(int(self.wait_for_element(self.PAGE_LENGHT).text) - 1):
            self.PRODUCTS_NAME = self.presence_for_elements(self.PRODUCT_NAME_SELECTOR)
            self.PRODUCTS_PRICE = self.presence_for_elements(self.PRODUCT_PRICE_SELECTOR)
            for x in range(len(self.PRODUCTS_NAME)):
                self.BOOK_INFO = str(str(x + 1) + " : Name : " + self.PRODUCTS_NAME[x].text + " Price : " + self.PRODUCTS_PRICE[x].text + "\n")
                self.TXTDOC = (self.TXTDOC + self.BOOK_INFO)
            self.scroll_specific_height(10000)
            self.click(self.NEXT_PAGE)
            time.sleep(0.350)
        return self.TXTDOC
