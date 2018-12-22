from selenium.webdriver.common.by import By


class InternalPageLocators:
# TOP NAVIGATOR
    MENU_SIGNIN_BUTTON = (By.CSS_SELECTOR, "span[class*='_signin_'")
    MENU_USER_ICON = (By.XPATH, "//div[@class='ow_console_items_wrap']/div[5]")
    MENU_USER_LOGOUT = (By.XPATH, "//a[contains(@href,'sign-out')]")
    MY_DASHBOARD_TEXT = (By.CSS_SELECTOR, "h1[class*='ow_ic_house']")

# SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
    SIGN_IN_MENU = (By.CSS_SELECTOR, "a[class*='console'][href*='/user/']")
    SIGN_OUT_MENU = (By.CSS_SELECTOR, "a[href*='sign-out']")

    USER_MENU = (By.CSS_SELECTOR, "div[class*='dropdown_hover']")


# NEWSFEED
NEWSFEED_TEXTAREA = (By.XPATH, "//*[@name='status']")
NEWSFEED_SAVE_BUTTON = (By.XPATH, "//*[@name='save']")
NEWSFEED_MESSAGES = (By.XPATH, "//*[@class='ow_newsfeed_content']")
NEWSFEED_MESSAGES_CONTENT = (By.CSS_SELECTOR, "div.ow_newsfeed_context_menu_wrap")
NEWSFEED_MESSAGES_MORE = (By.CSS_SELECTOR, "span.ow_context_more")
NEWSFEED_MESSAGES_DELETE = (By.CSS_SELECTOR, "a[class*='newsfeed_remove_btn']")



# Login windows locators
SIGNIN_USERNAME = (By.CSS_SELECTOR, "input[name='identity']")
SIGNIN_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
SIGNIN_REMEMBER_CHECKBOX = (By.CSS_SELECTOR, "input[name='remember']")
SIGNIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[name='submit']")

LOGIN_FIELD = (By.NAME, 'identity')
PASS_FIELD = (By.NAME, 'password')


LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")