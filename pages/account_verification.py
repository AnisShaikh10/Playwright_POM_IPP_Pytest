from playwright.sync_api import Page, expect
from .base_page import BasePage

class AccountVerificationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def email_verification_message(self):
        return self.page.get_by_text("Account verified - thank you")
    
    @property
    def continue_button(self):
        return self.page.get_by_role("button", name="Continue")
    
    @property
    def view_button(self):
        return self.page.get_by_role("link", name="View")
    
    def verify_account(self):
        self.wait_for_element(self.email_verification_message, timeout=30000)
        self.assert_element_is_visible(self.email_verification_message)
        # expect(self.email_verification_message).to_be_visible()
        self.click_element(self.continue_button)
        self.click_element(self.view_button)
    

