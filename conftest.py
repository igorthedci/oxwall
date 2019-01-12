import json
import os.path
import pytest
from selenium import webdriver
from oxwall_site_model import OxwallSite
from value_models.user import User


@pytest.fixture(scope="session")
def driver(selenium):
    # Open browser driver settings
    driver = selenium
    driver.implicitly_wait(5)
    # driver.maximize_window()
    driver.get('http://127.0.0.1/oxwall/')
    yield driver
    # Close browser
    driver.quit()


@pytest.fixture()
def app():
    app = OxwallSite()
    yield app
    # app.close()
    pass


@pytest.fixture()
def login_user(app):
    app.login('admin', 'Adm1n')
    yield
    app.logout()


@pytest.fixture
def admin_user():
    return User(username='admin', password='Adm1n', real_name='Admin', is_admin=True)


# user_data = [
#     {
#         "username": "tester",
#         "password": "secret",
#         "real_name": "How I am?",
#         "is_admin": False
#      },
#     {
#         "username": "tester",
#         "password": "secret",
#         "real_name": "How I am?",
#         "is_admin": False
#      },
#     {
#         "username": "admin",
#         "password": "Adm1n",
#         "real_name": "ADMIN",
#         "is_admin": True
#      }
# ]

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PROJECT_DIR, "data", "user_data.json")) as f:
    user_data = json.load(f)


@pytest.fixture(params=user_data, ids=[str(user) for user in user_data])
def user(request):
    return User(**request.param)  # TODO: parametrize to non-admin users


# @pytest.fixture()
# def sign_in_session(app, admin_user):
#     app.login_as(admin_user)
#     yield user
#     app.logout_as(admin_user)


@pytest.fixture()
def signed_in_user(driver, user):
    app = OxwallSite(driver)
    app.login_as(user)
    yield user
    app.logout_as(user)


@pytest.fixture()
def logout(driver):
    yield
    app = OxwallSite(driver)
    app.dash_page.sign_out()
