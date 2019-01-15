from datetime import datetime

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
        # self.driver.get('http://127.0.0.1/oxwall/')
        self.wait = WebDriverWait(self.driver, 5)
        self.actions = ActionChains(self.driver)

        self.main_page = MainPage(self.driver)
        self.dash_page = DashboardPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)

    def login_as(self, user):
        """ Login to Oxwall site by user"""
        self.main_page.sign_in_menu.click()
        self.sign_in_page.input_username(user.username)
        self.sign_in_page.input_password(user.password)
        self.sign_in_page.submit_form()

    def logout_as(self, user):
        # TODO: add user_name assert
        menu = self.main_page.user_menu
        self.actions.move_to_element(menu).perform()
        self.main_page.sign_out_link.click()

    def add_new_text_status(self, status):
        driver = self.driver
        # Write some text to Newsfeed form and send it
        newsfeed = driver.find_element_by_name("status")
        # newsfeed.click()
        newsfeed.clear()
        # newsfeed.click()
        newsfeed.send_keys(status.text)
        send_button = driver.find_element_by_name("save")
        send_button.click()
        # status.time_created = datetime.now()
