from playwright.sync_api import Page, expect
from utils.data_generator import UserProfile
from .base_page import BasePage

class CreateUserPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
    @property
    def title_selector(self):
        return self.page.get_by_label("Title")

    @property
    def firstname_input(self):
        return self.page.get_by_role("textbox", name="First Name")

    @property
    def lastname_input(self):
        return self.page.get_by_role("textbox", name="Family Name *")

    @property
    def dob_input(self):
        return self.page.get_by_role("textbox", name="Date of Birth *")

    @property
    def gender_selector(self):
        return self.page.get_by_label("Gender")

    @property
    def email_input(self):
        # Try Email Address first
        locator = self.page.get_by_role("textbox", name="Email Address*")
        if locator.count() > 0:
            return locator
        else:
            # Fallback to Username
            return self.page.get_by_role("textbox", name="* Username")

    @property
    def confirm_email_input(self):
        return self.page.get_by_role("textbox", name="Confirm Email Address *")

    @property
    def password_input(self):
        return self.page.get_by_role("textbox", name="Password*", exact=True)

    @property
    def confirm_password_input(self):
        return self.page.get_by_role("textbox", name="Confirm Password*")

    @property
    def consent_checkbox(self):
        return self.page.locator("//span[contains(text(), 'I consent to allowing the university to process my data')]")

    @property
    def referee_consent_checkbox(self):
        return self.page.locator("//span[contains(text(), 'I consent to allowing the university to contact my')]")

    @property
    def submit_button(self):
        return self.page.get_by_role("button", name="Create User")
    

    @property
    def success_message(self):
        primary = self.page.get_by_text("Thank you for applying.")
        alternate = self.page.get_by_text("Thank you for creating an account")

        # Try primary first
        try:
            primary.wait_for(state="visible", timeout=3000)
            return primary
        except:
            # fallback
            alternate.wait_for(state="visible", timeout=3000)
            return alternate

    @property
    def continue_application_button(self):
        return self.page.get_by_role("link", name="Continue my Application")

    # -------------------------
    #       Page Actions
    # -------------------------
    def navigate_to_ipp_link(self, url):
        self.navigate(url)

    def fill_user_details(self, user_profile: UserProfile):
        """Fill all personal details using the provided UserProfile"""
        self.select_option(self.title_selector, user_profile.title)
        self.fill_input(self.firstname_input, user_profile.first_name)
        self.fill_input(self.lastname_input, user_profile.last_name)
        self.fill_input(self.dob_input, user_profile.dob)
        self.select_option(self.gender_selector, user_profile.gender)
        self.fill_input(self.email_input, user_profile.email)
        self.fill_input(self.confirm_email_input, user_profile.email)
        self.fill_input(self.password_input, "Infuse@12345")
        self.fill_input(self.confirm_password_input, "Infuse@12345")
        # check consents
        self.click_element(self.consent_checkbox)
        self.click_element(self.referee_consent_checkbox)

    def submit_form(self):
        self.click_element(self.submit_button)

    def expect_success_message(self):
        self.wait_for_element(self.success_message, timeout=30000)
        self.assert_element_is_visible(self.success_message)

    def continue_application(self):
        self.click_element(self.continue_application_button)