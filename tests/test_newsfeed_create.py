import pytest

from oxwall_site_model import OxwallSite
from value_models.status import Status
from data.status_data import status_data

# status_data = ["alfa098tEXT", "Привіт", "!№:41!6№!"]


@pytest.mark.parametrize("status_text", status_data, ids=["Alphanum", "Cyrillic", "Symbols"])
def test_add_text_status(driver, signed_in_user, status_text):
    app = OxwallSite(driver)
    status = Status(text=status_text, user=signed_in_user)
    # old_status_list = app.dash_page.status_list

    # app.dash_page.status_text_field.send_keys(status.text)
    assert app.dash_page.status_text_field.placeholder == "QQQ"
    app.dash_page.status_text_field.input(status.text)
    app.dash_page.send_button.click()
    app.dash_page.wait_until_new_status_appeared()

    new_status = app.dash_page.status_list[0]
    assert new_status.text == status.text
    assert new_status.user == signed_in_user.real_name()
    assert new_status.time == "within 1 minute"

    # app.add_new_text_status(status)
    # app.wait_until_new_status_appeared()
    # # Verification that new status with this text appeared

    # text_elements = app.get_newsfeed_list()
    # user_status_elements = app.get_status_users()
    # time_status_elements = app.get_status_users()
    # assert status_block.status_text == status.text
    # assert status_block.user_element.text == status.user.real_name
    # assert status_block.time_element.text == "within 1 minute"
