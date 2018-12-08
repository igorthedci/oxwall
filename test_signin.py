import pytest


account_list = [
    # ("", "", False),
    ("admin", "Adm1n", True),
    # ("", "admin", False),
    ("admin", "admin", False)
]


@pytest.mark.parametrize("username, password, expected_result", account_list)
def test_signin(app, username, password, expected_result):

    actual_result = app.login(username, password)

    # Verifications
    assert actual_result == expected_result

    if actual_result:
        app.logout()

