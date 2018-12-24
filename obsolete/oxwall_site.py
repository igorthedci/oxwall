from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_objects import newsfeed_page


class Oxwall:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        # self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/oxwall/')
        self.wait = WebDriverWait(self.driver, 6)
        self.actions = ActionChains(self.driver)

        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/oxwall/')
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)
        try:
            self.wait.until(EC.visibility_of_element_located(newsfeed_page.MENU_SIGNIN_BUTTON))
        except TimeoutException:
            pass  # no the main page

    def close(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(*newsfeed_page.MENU_SIGNIN_BUTTON).click()
        login = self.driver.find_element(*newsfeed_page.SIGNIN_USERNAME)
        login.send_keys(username)
        passw = self.driver.find_element(*newsfeed_page.SIGNIN_PASSWORD)
        passw.send_keys(password)

        element = self.driver.find_element(*newsfeed_page.SIGNIN_REMEMBER_CHECKBOX)
        if element.get_attribute('checked'):
            element.click()

        self.driver.find_element(*newsfeed_page.SIGNIN_SUBMIT_BUTTON).click()

        try:
            self.wait.until(EC.visibility_of_element_located(newsfeed_page.MENU_USER_ICON))
            return True
        except TimeoutException:
            self.actions.send_keys(Keys.ESCAPE).perform()
            return False

    def logout(self):
        # menu = self.driver.find_element(By.LINK_TEXT, user.title())
        menu_user = self.driver.find_element(*newsfeed_page.MENU_USER_ICON)
        self.actions.move_to_element(menu_user).perform()
        self.driver.find_element(*newsfeed_page.MENU_USER_LOGOUT).click()

    def create_comment(self, app, test_text):
        newsfeed = app.driver.find_element(*newsfeed_page.NEWSFEED_TEXTAREA)
        # newsfeed.click()
        newsfeed.clear()
        # newsfeed.click()
        newsfeed.send_keys(test_text)
        send_button = app.driver.find_element(*newsfeed_page.NEWSFEED_SAVE_BUTTON)
        send_button.click()

    def get_comments(self):
        return self.driver.find_elements(*newsfeed_page.NEWSFEED_MESSAGES)

    def open_user_profile(self):
        pass

