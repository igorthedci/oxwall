from selenium.webdriver.common.by import By

from page_objects.internal_page import InternalPage
from page_objects.page import InputTextElement


class JoinPage(InternalPage):

    TITLE_LOCATOR = (By.CSS_SELECTOR, "h1.ow_ic_file")
    USERNAME_TITLE = (By.CSS_SELECTOR, "tr:nth-of-type(6) label")
    USERNAME_FIELD = (By.CSS_SELECTOR, "tr:nth-of-type(6) input")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    REPEATPASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='repeatPassword']")
    REALNAME_FIELD = (By.CSS_SELECTOR, "tr:nth-of-type(15) input")
    GENDER_MALE = (By.CSS_SELECTOR, 'tr:nth-of-type(18) li>input[value="1"]')
    GENDER_FEMALE = (By.CSS_SELECTOR, 'tr:nth-of-type(18) li>input[value="2"]')
    BD_DAY_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(24) select[name*="day"]')
    BD_MONTH_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(24) select[name*="month"]')
    BD_YEAR_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(24) select[name*="year"]')
    FOR_MALE_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(35) li>input[value="1"]')
    FOR_FEMALE_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(35) li>input[value="2"]')
    FOR_FUN_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(35) li>input[value="1"]')
    FOR_FRIENDSHIP_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(35) li>input[value="8"]')
    FOR_DATING_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(35) li>input[value="4"]')
    FOR_WHATEVER_FIELD = (By.CSS_SELECTOR, 'tr:nth-of-type(35) li>input[value="2"]')
    MUSIC_INTEREST = (By.CSS_SELECTOR, 'tr:nth-of-type(44) textarea')
    BOOK_INTEREST = (By.CSS_SELECTOR, 'tr:nth-of-type(50) textarea')

    JOIN_BUTTON = (By.NAME, "joinSubmit")

    # TODO Add all elements and actions that you have in Main Page

    def is_this_page(self):
        return self.active_menu.text == "DASHBOARD"

    @property
    def status_text_field(self):
        return InputTextElement(self.find_visible_element(self.STATUS_TEXT_FIELD))
        # return self.find_visible_element(self.STATUS_TEXT_FIELD)

    @property
    def send_button(self):
        return self.find_visible_element(self.SEND_BUTTON)

    @property
    def status_list(self):
        return [StatusElement(el) for el in self.driver.find_elements(*self.STATUS_BOX)]

    def wait_until_new_status_appeared(self):
        old_number = len(self.status_list)
        self.wait.until(amount_of_element_located(self.STATUS_BOX, old_number+1), "No new status detected")

