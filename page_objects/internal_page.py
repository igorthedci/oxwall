from selenium.common.exceptions import NoSuchElementException
# from locators.locator import InternalPageLocators as locators
from selenium.webdriver.common.by import By

from page_objects.page import Page


class InternalPage(Page):

    # LOCATORS
    ACTIVE_MENU = (By.XPATH, "//div[contains(@class, 'ow_menu_wrap')]//li[contains(@class, 'active')]")
    DASHBOARD_MENU = (By.LINK_TEXT, "DASHBOARD")
    MAIN_MENU = (By.LINK_TEXT, "MAIN")
    PHOTO_MENU = ()  # TODO

    # TODO Add other menu locators
    SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
    SIGN_UP_MENU = (By.CSS_SELECTOR, 'a.ow_console_item_link[href*="join"]')
    USER_MENU = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")
    SIGN_OUT_LINK = (By.XPATH, './/a[contains(@href,"sign-out")]')

    def __init__(self, driver):
        super().__init__(driver)
        # self.sign_in_menu = self.find_visible_element(locators.SIGN_IN_MENU)

    def is_logged_in(self):
        return self.is_element_present(self.USER_MENU)

    def is_logged_in_as(self, user):
        return self.user_menu.text == user.username.title()

    @property
    def active_menu(self):
        return self.find_visible_element(self.ACTIVE_MENU)

    @property
    def dashboard_menu(self):
        return self.find_visible_element(self.DASHBOARD_MENU)

    @property
    def main_menu(self):
        return self.find_visible_element(self.MAIN_MENU)

    # TODO Add other Nav menu

    @property
    def sign_in_menu(self):
        locator = self.SIGN_IN_MENU
        if not self.is_logged_in():
            return self.find_visible_element(locator)
        else:
            raise NoSuchElementException("No element by locator {}".format(locator))

    @property
    def sign_up_menu(self):
        # TODO по аналогии с предыдущим
        return

    @property
    def user_menu(self):
        locator = self.USER_MENU
        if self.is_logged_in():
            return self.find_visible_element(locator)
        else:
            raise NoSuchElementException("No element by locator {}".format(locator))

    @property
    def sign_out_link(self):
        return self.find_visible_element(self.SIGN_OUT_LINK)

    # Nav Actions:
    def sign_out(self):
        self.action_chain.move_to_element(self.user_menu).perform()
        self.sign_out_link.click()

    def go_main_page(self):
        self.main_menu.click()

    def go_signin_page(self):
        self.sign_in_menu.click()

    # TODO you can do other actions that are common to all internal pages
