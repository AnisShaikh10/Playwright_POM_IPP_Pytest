from pages.login_page import LoginPage
# from conftest import page
import time


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    time.sleep(5)

    # simple assertion example
    assert page.url == "https://www.saucedemo.com/inventory.html"