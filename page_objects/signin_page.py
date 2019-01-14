import time

from selenium.webdriver.support.expected_conditions import invisibility_of_element_located

from page_objects.dashboard_page import DashboardPage
from page_objects.page import Page
from page_objects.page_elements.input_text_field import InputTextElement


class SignInPage(Page):

    # Login windows locators
    SIGNIN_USERNAME = (By.CSS_SELECTOR, "input[name='identity']")
    SIGNIN_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    SIGNIN_REMEMBER_CHECKBOX = (By.CSS_SELECTOR, "input[name='remember']")
    SIGNIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[name='submit']")

    LOGIN_FIELD = (By.NAME, 'identity')
    PASS_FIELD = (By.NAME, 'password')

    LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")
    LOGIN_WINDOW_BOX = (By.CLASS_NAME, "floatbox_container")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error")
    ERROR_CLOSE_BUTTON = (By.CSS_SELECTOR, "a.close_button")

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.username_field = self.find_visible_element(locator.LOGIN_FIELD)
    #  Not good decision, because we can get staleness elements over time

    @property
    def username_field(self):
        return self.find_visible_element(self.LOGIN_FIELD)
        # return InputTextElement(self.find_visible_element(SignInLocators.LOGIN_FIELD))
        # return self.find_visible_element(SignInLocators.LOGIN_FIELD)

    @property
    def password_field(self):
        return self.find_visible_element(self.PASS_FIELD)
        # return self.find_visible_element(SignInLocators.PASS_FIELD)

    @property
    def sign_in_button(self):
        return self.find_visible_element(self.SIGNIN_SUBMIT_BUTTON)
        # return self.find_visible_element(SignInLocators.SIGN_IN_BUTTON)

    def is_this_page(self):
        return self.is_element_present(self.LOGIN_WINDOW_BOX)
        # return self.is_element_present(SignInLocators.LOGIN_WINDOW_BOX)

    def input_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def input_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def submit_form(self):
        self.sign_in_button.click()
        locator = self.LOGIN_BACKGROUND
        try:
            self.wait.until(invisibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException("No element by locator {}".format(locator))


if __name__ == "__main__":

    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall")

    from page_objects.main_page import MainPage
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()

    sign_in_page = SignInPage(driver)

    # 1st type of using:
    sign_in_page.username_field.input("admin")
    sign_in_page.password_field.input("Adm1n")
    sign_in_page.submit_form()
