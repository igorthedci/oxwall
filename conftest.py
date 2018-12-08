import pytest
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


