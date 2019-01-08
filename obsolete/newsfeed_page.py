from selenium.webdriver.common.by import By

from page_objects.page import Page


class NewsfeedPage(Page):

# NEWSFEED
NEWSFEED_TEXTAREA = (By.XPATH, "//*[@name='status']")
NEWSFEED_SAVE_BUTTON = (By.XPATH, "//*[@name='save']")
NEWSFEED_MESSAGES = (By.XPATH, "//*[@class='ow_newsfeed_content']")
NEWSFEED_MESSAGES_CONTENT = (By.CSS_SELECTOR, "div.ow_newsfeed_context_menu_wrap")
NEWSFEED_MESSAGES_MORE = (By.CSS_SELECTOR, "span.ow_context_more")
NEWSFEED_MESSAGES_DELETE = (By.CSS_SELECTOR, "a[class*='newsfeed_remove_btn']")


