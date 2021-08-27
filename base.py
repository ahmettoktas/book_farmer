from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseFunctions(object):
    """
    Base Functions for get input, click and click random element
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 90)

    def click(self, selector):
        """
        Wait for element and click
        :param str selector: locator of element to find and click
        """
        self.wait.until(ec.element_to_be_clickable(selector)).click()

    def presence_for_elements(self, selector):
        """
        Presence for elements to present
        :param str selector: locater of the element to find
        """
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def scroll_specific_height(self, specific_pixel):
        """
        Lowers the web page by a given pixel
        :param int specific_pixel: Random integer value you want to use specific pixel

        """
        self.driver.execute_script("window.scrollTo(0,{})".format(specific_pixel))

    def wait_for_element(self, selector):
        return self.wait.until(ec.presence_of_element_located(selector))

    def format(self, *args, **kwargs):  # known special case of str.format
        """
        S.format(*args, **kwargs) -> str

        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        pass

    def element_exists(self, selector):
        """
        Returns true if element present or return false if element not present
        :param selector: locator of the element to be checked for

        """
        try:
            self.wait.until(ec.element_to_be_clickable(selector))
            return True
        except TimeoutException:
            return False
