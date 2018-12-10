from oxwall_site_model import OxwallSite
from value_models.status import Status


def test_newsfeed_e2e1(driver, sign_in_session, admin_user):
    """
    STEPS:
    - open OXWALL === fixture
    - sign in as admin === fixture
    - add a news
    - check the news is visible
    - like/unlike the news
    - check the like is visible
    - add a comment the news
    - check the comment is visible
    - delete the comment
    - check it is absent
    - sign out

    :param driver:
    :param sign_in_session:
    :param admin_user:
    :return:
    """
    app = OxwallSite(driver)

    expected_status = Status(text="text", user=admin_user)
    app.add_new_text_status(expected_status)
    app.wait_until_new_status_appeared()

    # Verification that new status with this text appeared
    actual_status = app.get_status()
    # text_elements = app.get_newsfeed_list()
    # user_status_elements = app.get_status_users()
    # time_status_elements = app.get_status_users()
    assert actual_status.content == expected_status.content
    assert actual_status.username == admin_user.real_name
    # assert actual_status.time_element.text == "within 1 minute"

    app.like_status()
    liked_status = app.get_status()
    assert liked_status.like.counter == actual_status.like.counter + 1
    assert liked_status.like.is_liked == True
    assert admin_user.real_name in liked_status.like.string
