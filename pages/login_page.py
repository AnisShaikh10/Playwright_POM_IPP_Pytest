from playwright.sync_api import Page
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def username(self):
        return self.page.get_by_role("textbox", name="Username")
    
    @property
    def password(self):
        return self.page.get_by_role("textbox", name="Password")
    
    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Log in")
    
    @property
    def header(self):
        return self.page.get_by_role("heading", name="Applications")
    
    @property
    def view_button(self):
        return self.page.get_by_role("link", name="View")

    def navigate_to_login_page(self, url=None):
        self.navigate(url)

    def fill_login_details(self, username=None, password=None):
        self.fill_input(self.username, username)
        self.fill_input(self.password, password)
        self.click_element(self.login_button)

    def verify_login_successful(self):
        self.assert_element_is_visible(self.header)
        self.click_element(self.view_button)
    