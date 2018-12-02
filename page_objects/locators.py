from selenium.webdriver.common.by import By

# TOP NAVIGATOR
MENU_USER_ICON = (By.XPATH, "//div[@class='ow_console_items_wrap']/div[5]")
MENU_USER_LOGOUT = (By.XPATH, "//a[contains(@href,'sign-out')]")
SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
SIGN_OUT_MENU = ()


# NEWSFEED
NEWSFEED_TEXTAREA = (By.XPATH, "//*[@name='status']")
NEWSFEED_SAVE_BUTTON = (By.XPATH, "//*[@name='save']")
NEWSFEED_MESSAGES = (By.XPATH, "//*[@class='ow_newsfeed_content']")

# Login windows locators
LOGIN_FIELD = (By.NAME, 'identity')
PASS_FIELD = (By.NAME, 'password')
SIGN_IN_BUTTON = (By.XPATH, "//div[@class='ow_right']")


LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")