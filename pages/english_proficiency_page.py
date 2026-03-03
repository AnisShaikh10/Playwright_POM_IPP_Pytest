from playwright.sync_api import Page
from pages.base_page import BasePage

class EnglishProficiencyPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='English Proficiency']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_english_proficiency_button(self):
        return self.page.get_by_role("link", name="Edit English Proficiency")

    @property
    def english_language_test_dropdown(self):
        return self.page.get_by_label("Have you sat a relevant")
    
    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    
    def edit_english_proficiency(self):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_english_proficiency_button)
            self.select_option(self.english_language_test_dropdown, "No")
            self.click_element(self.next_button)
        else:
            print("English Proficiency section is already complete, proceeding to next section")