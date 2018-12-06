import time

from page_objects import locators


def test_comment_delete(app, login_user):
    message_box = app.driver.find_elements(*locators.NEWSFEED_MESSAGES_CONTENT)[0]
    time.sleep(2)
    message_box.click()
    more_button = message_box.find_element(*locators.NEWSFEED_MESSAGES_MORE)
    time.sleep(2)
    more_button.click()
    # delete_button = message_box.find_element(*locators.NEWSFEED_MESSAGES_DELETE)
    delete_button = message_box.find_element(*locators.NEWSFEED_MESSAGES_DELETE)
    delete_button.click()
    time.sleep(2)
    try:
        wait.until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")
    try:
        delete_button.click()
    except UnexpectedAlertPresentException:
    time.sleep(3)

    try:
        self.wait.until(EC.alert_is_present())
        return True
    except TimeoutException:
        self.actions.send_keys(Keys.ESCAPE).perform()
        return False
