from oxwall_site_model import OxwallSite
import time


def test_login_using_page_object(driver, user, logout):
    app = OxwallSite(driver)
    app.main_page.sign_in_click()
    assert app.sign_in_page.is_this_page()
    app.sign_in_page.username_field.input(user.username)
    app.sign_in_page.password_field.input(user.password)
    app.sign_in_page.submit_form()
    assert app.dash_page.is_this_page()
    assert app.dash_page.is_logged_in()
    assert app.dash_page.user_menu.text == user.real_name
    time.sleep(3.3)
    app.logout_as(user)


def test_admin_login_logout(driver, admin_user):
    app = OxwallSite(driver)
    app.main_page.go_signin_page()
    assert app.sign_in_page.is_this_page()
    app.sign_in_page.input_username(admin_user.username)
    app.sign_in_page.input_password(admin_user.password)
    app.sign_in_page.submit_form()

    assert app.dash_page.is_this_page()
    assert app.dash_page.is_logged_in()
    assert app.dash_page.user_menu.text == admin_user.real_name
    time.sleep(1.1)

    app.logout_as(admin_user)
