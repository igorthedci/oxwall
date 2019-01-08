import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

from page_objects.dashboard_page import DashboardPage
from page_objects.main_page import MainPage
from page_objects.signin_page import SignInPage


class OxwallSite:
    def __init__(self, driver):
        # Open Oxwall site
        self.driver = driver
        self.driver.get('http://127.0.0.1/oxwall/')
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

        self.main_page = MainPage(self.driver)
        self.dash_page = DashboardPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)

    def login_as(self, user):
        """ Login to Oxwall site by user"""
        # driver = self.driver
        self.main_page.sign_in_menu.click()
        # driver.find_element(*InternalPageLocators.SIGN_IN_MENU).click()
        self.sign_in_page.input_username(user.username)
        self.sign_in_page.input_password(user.password)
        self.sign_in_page.submit_form()
        # login = driver.find_element(*SignInLocators.LOGIN_FIELD)
        # login.click()
        # login.send_keys(user.username)
        # passw = driver.find_element(*SignInLocators.PASS_FIELD)
        # passw.click()
        # passw.send_keys(user.password)
        # driver.find_element(*SignInLocators.SIGN_IN_BUTTON).click()
        # Wait until grey background disappeared
        # wait = WebDriverWait(driver, 5)
        # wait.until(EC.invisibility_of_element_located(SignInLocators.LOGIN_BACKGROUND))

    def logout_as(self, user):
        menu = self.driver.find_element(By.LINK_TEXT, user["username"].title())
        self.actions.move_to_element(menu).perform()
        self.driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()

    def add_new_text_status(self, status):
        driver = self.driver
        # Write some text to Newsfeed form and send it
        newsfeed = driver.find_element_by_name("status")
        newsfeed.click()
        newsfeed.clear()
        newsfeed.click()
        newsfeed.send_keys(status.text)
        send_button = driver.find_element_by_name("save")
        send_button.click()
        status.time_created = datetime.now()

    def wait_until_new_status_appeared(self):
        # Wait until new status appear
        time.sleep(2)

    def get_newsfeed_list(self):
        return self.driver.find_elements_by_class_name("ow_newsfeed_content")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_dashboard_page(self):
        time.sleep(3)
        return self.is_element_present(By.XPATH, "/html/body/div[1]/div[4]/div/div/div/h1")

    def get_newsfeed_users(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "div.ow_newsfeed_string.ow_small.ow_smallmargin > a")

    def get_newsfeed_times(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "div.ow_newsfeed_btns.ow_small.ow_remark.clearfix > a")