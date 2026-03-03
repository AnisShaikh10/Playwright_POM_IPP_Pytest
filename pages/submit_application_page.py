import re
from playwright.sync_api import Page
from pages.base_page import BasePage
import time

class SubmitApplicationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    
    @property
    def submit_application_button(self):
        return self.page.get_by_role("link", name="Submit Application")

    @property
    def tearms_and_condition_check(self):
        return self.page.get_by_text("I have read, understand and")
    
    @property
    def submit_button(self):
        return self.page.get_by_role("button", name="Submit")
    
    @property
    def message(self):
        return self.page.get_by_text("Thank you for submitting your")
    
    @property
    def continue_button(self):
        return self.page.get_by_role("button", name="Continue")
    
    @property
    def profile_icon(self):
        return self.page.get_by_role("button", name="View Profile Details")
    
    @property
    def applicant_id(self):
        return self.page.locator("div.sv-text-center.sv-center-block")
    
    def submit_application(self):
        self.click_element(self.submit_application_button)
        self.click_element(self.tearms_and_condition_check)
        self.click_element(self.submit_button, delay=2000)
        self.wait_for_element(self.message, timeout=100000)
        self.assert_element_is_visible(self.message)
        self.click_element(self.continue_button)
        self.click_element(self.profile_icon)
        student_info = self.applicant_id.inner_text()
        print(student_info)
        text = student_info
        match = re.search(r"\((\d+)\)", text)
        if match:
            applicant_id = match.group(1)
            print(applicant_id)  # Output: 26103623
        return student_info, applicant_id
