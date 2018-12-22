from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.action = ActionChains(driver)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException as e:

    def is_element_present(self, locator):
        try:
            element = app.driver.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def find_visible_element(self, locator):
        return self.wait.until(visibility_of_element_located(locator))

    def find_clicable_element(self, locator):
        return

    @property
    def current_url(self):
        return self.driver.current_url
    def find_clickable_element(self, locator):
        return self.wait.until(clickability_of_element_located(locator))

