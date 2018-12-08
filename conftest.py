import pytest
<<<<<<< HEAD
from selenium import webdriver
from oxwall_site_model import OxwallSite
from value_models.user import User


@pytest.fixture()
def driver():
    # Open browser driver settings
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('http://127.0.0.1/oxwall/')
    yield driver
    # Close browser
    driver.quit()

# @pytest.fixture()
# def app(driver):
#     app = OxwallSite(driver)
#     return app

@pytest.fixture()
def admin_user():
    return User(username="admin", password="pass")


@pytest.fixture()
def user():
    return User(username="admin", password="pass") # TODO: parametrize to non-admin users

@pytest.fixture()
def sign_in_session(app, admin_user):
    app.login_as(admin_user)
    yield
    app.logout_as(admin_user)
=======
from oxwall_site import Oxwall


@pytest.fixture()
def app():
    app = Oxwall()
    yield app
    # app.close()
    pass


@pytest.fixture()
def login_user(app):
    app.login('admin', 'Adm1n')
    yield
    app.logout()

@pytest.fixture()
def admin_user_old(app):
    return {'username': 'admin', 'password': 'Adm1n'}

@pytest.fixture
def admin_user():
    return User(username='admin', password='Adm1n')


>>>>>>> init commit
