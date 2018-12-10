from selenium.webdriver.common.by import By


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


class InternalPageLocators:
    OW_LOGO_MENU = (By.CSS_SELECTOR, "a[class*='ow_logo']")
    ACTIVE_MENU = (By.XPATH, "//div[contains(@class, 'ow_menu_wrap')]//li[contains(@class, 'active')]")

    DASHBOARD_MENU = (By.CSS_SELECTOR, "a[@href*='dashboard']")
    MAIN_MENU = (By.CSS_SELECTOR, "a[@href*='index']")
    MEMBERS_MENU = (By.CSS_SELECTOR, "a[@href*='users']")
    PHOTO_MENU = (By.CSS_SELECTOR, "a[@class*='photo']")
    VIDEO_MENU = (By.CSS_SELECTOR, "a[@href*='video']")

    # SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
    # SIGN_OUT_MENU = (By.XPATH, './/a[contains(@href,"sign-out")]')
    SIGN_IN_MENU = (By.CSS_SELECTOR, "a[class*='console'][href*='/user/']")
    SIGN_OUT_MENU = (By.CSS_SELECTOR, "a[href*='sign-out']")

    MESSAGES_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
    BELL_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
    USER_MENU = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")
    ADMIN_MENU = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")

    USER_MENU_PROFILE_INFO = ()
    USER_MENU_PROFILE_EDIT = ()
    USER_MENU_PREFERENCES = ()
    USER_MENU_NOTIFICATIOS = ()
    USER_MENU_SIGNOUT = (By.XPATH, "//a[contains(@href,'sign-out')]")

    MENU_SIGNIN_BUTTON = (By.CSS_SELECTOR, "span[class*='_signin_'")
    MENU_USER_ICON = (By.XPATH, "//div[@class='ow_console_items_wrap']/div[5]")



class SignInLocators:
    LOGIN_FIELD = (By.NAME, 'identity')
    PASS_FIELD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.XPATH, "//div[@class='ow_right']")
    LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")



# Newsfeed page_object ...

# Registration page_object ...
