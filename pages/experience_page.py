from playwright.sync_api import Page
from pages.base_page import BasePage

class ExperiencePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Experience']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_experience_button(self):
        return self.page.get_by_role("link", name="Edit Experience")

    @property
    def experience_dropdown(self):
        return self.page.get_by_label("Do you have any relevant work")

    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    
    def edit_experience(self):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.wait_for_element(self.edit_experience_button)
            self.click_element(self.edit_experience_button)
            self.select_option(self.experience_dropdown, "No")
            self.click_element(self.next_button)
        else:
            print("Experience section is already complete, proceeding to next section")