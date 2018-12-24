import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from page_objects import newsfeed_page


def test_comment_delete(app, login_user):
    message_box = app.driver.find_elements(*newsfeed_page.NEWSFEED_MESSAGES_CONTENT)[0]
    # time.sleep(2)
    message_box.click()
    more_button = message_box.find_element(*newsfeed_page.NEWSFEED_MESSAGES_MORE)
    # time.sleep(2)
    more_button.click()
    # delete_button = message_box.find_element(*locators.NEWSFEED_MESSAGES_DELETE)
    delete_button = message_box.find_element(*newsfeed_page.NEWSFEED_MESSAGES_DELETE)
    delete_button.click()
    # time.sleep(2)
    try:
        app.wait.until(EC.alert_is_present())
        alert = app.driver.switch_to.alert
        alert.accept()
        return True
    except TimeoutException:
        print("no alert")
        return False
