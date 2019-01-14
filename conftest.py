import json
import os.path
import pytest

from db.db_connector import DBConnector
from oxwall_site_model import OxwallSite
from value_models.user import User


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PROJECT_DIR, "config.json")) as f:
    config = json.load(f)


@pytest.fixture(scope="session")
def driver(selenium, base_url):
    # Open browser driver settings
    driver = selenium
    driver.implicitly_wait(5)
    # driver.maximize_window()
    driver.get(base_url)
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


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PROJECT_DIR, "data", "user_data.json")) as f:
    user_data = json.load(f)


@pytest.fixture(scope="session")
def db():
    db = DBConnector(config["db"])
    yield db
    db.close()
    # db.connection.close()


@pytest.fixture(params=user_data, ids=[str(user) for user in user_data])
def user(request, db):
    user = User(**request.param)  # TODO: parametrize to non-admin users
    db.create_user(user)
    yield user
    db.delete_user(user)


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
