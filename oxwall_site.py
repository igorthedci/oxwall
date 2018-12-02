from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_objects import locators


class Oxwall:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/oxwall/')
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def close(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(*locators.SIGN_IN_MENU).click()
        login = self.driver.find_element(*locators.LOGIN_FIELD)
        login.click()
        login.send_keys(username)
        passw = self.driver.find_element(*locators.PASS_FIELD)
        passw.click()
        passw.send_keys(password)
        self.driver.find_element(*locators.SIGN_IN_BUTTON).click()

        self.wait.until(EC.visibility_of_element_located(locators.MENU_USER_ICON))
        # self.wait.until(EC.invisibility_of_element_located(locators.LOGIN_BACKGROUND))
        # wait.until_not(EC.visibility_of_element_located((By.ID, "floatbox_overlay")))

    def logout(self, user):
        # menu = self.driver.find_element(By.LINK_TEXT, user.title())
        menu_user = self.driver.find_element(*locators.MENU_USER_ICON)
        self.actions.move_to_element(menu_user).perform()
        self.driver.find_element(*locators.MENU_USER_LOGOUT).click()

    def create_comment(self, app, test_text):
        newsfeed = app.driver.find_element(*locators.NEWSFEED_TEXTAREA)
        # newsfeed.click()
        newsfeed.clear()
        # newsfeed.click()
        newsfeed.send_keys(test_text)
        send_button = app.driver.find_element(*locators.NEWSFEED_SAVE_BUTTON)
        send_button.click()

    def get_comments(self):
        return self.driver.find_elements(*locators.NEWSFEED_MESSAGES)

