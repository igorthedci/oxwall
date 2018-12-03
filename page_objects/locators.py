from selenium.webdriver.common.by import By

# TOP NAVIGATOR
MENU_SIGNIN_BUTTON = (By.CSS_SELECTOR, "span[class*='_signin_'")
MENU_USER_ICON = (By.XPATH, "//div[@class='ow_console_items_wrap']/div[5]")
MENU_USER_LOGOUT = (By.XPATH, "//a[contains(@href,'sign-out')]")

# SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
SIGN_IN_MENU = (By.CSS_SELECTOR, "a[class*='console'][href*='/user/']")
SIGN_OUT_MENU = (By.CSS_SELECTOR, "a[href*='sign-out']")


# NEWSFEED
NEWSFEED_TEXTAREA = (By.XPATH, "//*[@name='status']")
NEWSFEED_SAVE_BUTTON = (By.XPATH, "//*[@name='save']")
NEWSFEED_MESSAGES = (By.XPATH, "//*[@class='ow_newsfeed_content']")


# Login windows locators
SIGNIN_USERNAME = (By.CSS_SELECTOR, "input[name='identity']")
SIGNIN_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
SIGNIN_REMEMBER_CHECKBOX = (By.CSS_SELECTOR, "input[name='remember']")
SIGNIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[name='submit']")

LOGIN_FIELD = (By.NAME, 'identity')
PASS_FIELD = (By.NAME, 'password')


LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")