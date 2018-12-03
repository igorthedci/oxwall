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


