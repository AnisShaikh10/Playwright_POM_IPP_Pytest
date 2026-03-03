from playwright.sync_api import Page
from .base_page import BasePage

class PersonalDetailsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    
    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Personal Details']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_personal_details_button(self):
        return self.page.get_by_role("link", name="Edit Personal Details")
    
    @property
    def previously_applied(self):
        return self.page.locator("//label[contains(text(),'Have you previously applied')]/following::select[1]")
    
    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    def edit_personal_details(self):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_personal_details_button)
            self.select_option(self.previously_applied, "No")
            self.click_element(self.next_button)
        else:
            print("Personal details section is already complete, proceeding to next section")
        