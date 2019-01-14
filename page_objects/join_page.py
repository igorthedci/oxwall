import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.internal_page import InternalPage


class JoinPage(InternalPage):

    TITLE_LOCATOR = (By.CSS_SELECTOR, "h1.ow_ic_file")

    USERNAME_TITLE = (By.XPATH, '//label[text()="Username"]')
    USERNAME_FIELD = (By.XPATH, '//label[text()="Username"]/../..//input')
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/../..//input')
    PASSWORD_FIELD = (By.XPATH, '//label[text()="Password"]/../..//input')
    REPEATPASSWORD_FIELD = (By.XPATH, '//label[text()="Repeat password"]/../..//input')
    REALNAME_FIELD = (By.XPATH, '//label[text()="Real name"]/../..//input')

    GENDER_MALE = (By.XPATH, '//label[text()="Gender"]/../..//label[text()="Male"]/..//input')
    GENDER_FEMALE = (By.XPATH, '//label[text()="Gender"]/../..//label[text()="Female"]/..//input')

    BD_DAY_FIELD = (By.CSS_SELECTOR, 'select[name*="day"]')
    BD_MONTH_FIELD = (By.CSS_SELECTOR, 'select[name*="month"]')
    BD_YEAR_FIELD = (By.CSS_SELECTOR, 'select[name*="year"]')

    FOR_MALE_FIELD = (By.XPATH, '//label[text()="Looking for"]/../..//label[text()="Male"]/..//input')
    FOR_FEMALE_FIELD = (By.XPATH, '//label[text()="Looking for"]/../..//label[text()="Female"]/..//input')

    FOR_FUN_FIELD = (By.XPATH, '//label[text()="Here for"]/../..//label[text()="Fun"]/..//input')
    FOR_FRIENDSHIP_FIELD = (By.XPATH, '//label[text()="Here for"]/../..//label[text()="Friendship"]/..//input')
    FOR_DATING_FIELD = (By.XPATH, '//label[text()="Here for"]/../..//label[text()="Dating"]/..//input')
    FOR_WHATEVER_FIELD = (By.XPATH, '//label[text()="Here for"]/../..//label[text()="Whatever"]/..//input')

    MUSIC_INTEREST = (By.XPATH, '//label[text()="Music"]/../..//textarea')
    BOOK_INTEREST = (By.XPATH, '//label[text()="Favorite books"]/../..//textarea')
    # USER_PHOTO = (By.CSS_SELECTOR, 'for the future')

    JOIN_BUTTON = (By.CSS_SELECTOR, 'span.ow_ic_submit')

    # TODO Add all elements and actions that you have in Main Page

    @property
    def username_field(self):
        return self.select_valid_element(self.USERNAME_FIELD)

    @property
    def email_field(self):
        return self.select_valid_element(self.EMAIL_FIELD)

    @property
    def password_field(self):
        return self.select_valid_element(self.PASSWORD_FIELD)

    @property
    def repeatpassword_field(self):
        return self.select_valid_element(self.REPEATPASSWORD_FIELD)

    @property
    def realname_field(self):
        return self.select_valid_element(self.REALNAME_FIELD)

    @property
    def gender_male_field(self):
        return self.select_valid_element(self.GENDER_MALE)

    @property
    def gender_female_field(self):
        return self.select_valid_element(self.GENDER_FEMALE)

    @property
    def birthday_day_field(self):
        return self.select_valid_element(self.BD_DAY_FIELD)

    @property
    def birthday_month_field(self):
        return self.select_valid_element(self.BD_MONTH_FIELD)

    @property
    def birthday_year_field(self):
        return self.select_valid_element(self.BD_YEAR_FIELD)

    @property
    def looking_for_male_field(self):
        return self.select_valid_element(self.FOR_MALE_FIELD)

    @property
    def looking_for_female_field(self):
        return self.select_valid_element(self.FOR_FEMALE_FIELD)

    @property
    def here_for_fun_field(self):
        return self.select_valid_element(self.FOR_FUN_FIELD)

    @property
    def here_for_friendship_field(self):
        return self.select_valid_element(self.FOR_FRIENDSHIP_FIELD)

    @property
    def here_for_dating_field(self):
        return self.select_valid_element(self.FOR_DATING_FIELD)

    @property
    def here_for_whatever_field(self):
        return self.select_valid_element(self.FOR_WHATEVER_FIELD)

    @property
    def music_interest(self):
        return self.select_valid_element(self.MUSIC_INTEREST)

    @property
    def book_interest(self):
        return self.select_valid_element(self.BOOK_INTEREST)

    @property
    def join_button(self):
        return self.find_visible_element(self.JOIN_BUTTON)

    def input_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def input_email(self, email):
        self.email_field.clear()
        self.email_field.send_keys(email)

    def input_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)
        self.repeatpassword_field.clear()
        self.repeatpassword_field.send_keys(password)

    def input_realname(self, realname):
        self.realname_field.clear()
        self.realname_field.send_keys(realname)

    def input_gender(self, gender):
        gender_field = self.gender_female_field if gender.lower() in ['f', 'female', '2'] else self.gender_male_field
        gender_field.click()

    def input_birthday(self, birthday):  # BIRTHDAY
        locator = self.birthday_day_field
        locator.click()
        Select(locator).select_by_visible_text(str(birthday[0]))
        locator = self.birthday_month_field
        locator.click()
        Select(locator).select_by_visible_text(str(birthday[1]))
        locator = self.birthday_year_field
        locator.click()
        Select(locator).select_by_visible_text(str(birthday[2]))

    def input_looking_for(self, looking_for):
        if looking_for[0]:
            self.looking_for_male_field.click()
        if looking_for[1]:
            self.looking_for_female_field.click()

    def input_here_for(self, here_for):
        if here_for[0]:
            self.here_for_fun_field.click()
        if here_for[1]:
            self.here_for_friendship_field.click()
        if here_for[2]:
            self.here_for_dating_field.click()
        if here_for[3]:
            self.here_for_whatever_field.click()

    def input_music_interest(self, music):
        self.music_interest.clear()
        self.music_interest.send_keys(music)

    def input_book_interest(self, book):
        self.book_interest.clear()
        self.book_interest.send_keys(book)

    def submit_form(self):  # JOIN BUTTON
        self.join_button.click()
        # locator = self.LOGIN_BACKGROUND
        # try:
        #     self.wait.until(invisibility_of_element_located(locator))
        # except TimeoutException:
        #     raise NoSuchElementException("No element by locator {}".format(locator))


if __name__ == "__main__":

    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall")

    from page_objects.main_page import MainPage
    main_page = MainPage(driver)
    main_page.go_join_page()

    join_page = JoinPage(driver)

    random_string = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 14))

    join_page.input_username(random_string)
    email = 'qq' + random_string + '@gmail.com'
    join_page.input_email(email)
    join_page.input_password("pass1234")
    join_page.input_realname("The Tester")

    join_page.input_gender("Female")

    join_page.input_birthday([1, "Jan", 1991])
    # join_page.input_birthday([31, "Dec", 1930])

    join_page.input_looking_for([1, 1])
    join_page.input_here_for([1, 1, 0, 1])

    join_page.input_music_interest("Classic")
    join_page.input_book_interest("Python Guides")

    join_page.submit_form()
