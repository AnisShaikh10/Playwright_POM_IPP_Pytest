from playwright.sync_api import Page
from pages.base_page import BasePage

class PersonalStatementPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Personal Statement']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_personal_statement_button(self):
        return self.page.get_by_role("link", name="Edit Personal Statement")

    @property
    def personal_statement_dropdown(self):
        return self.page.get_by_label("Do you have a personal")

    @property
    def personal_statement_input(self):
        return self.page.get_by_role("textbox", name="Please type your personal")

    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    
    def edit_personal_statement(self, personal_statement):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.wait_for_element(self.edit_personal_statement_button)
            self.click_element(self.edit_personal_statement_button)
            self.select_option(self.personal_statement_dropdown, "No")
            self.fill_input_with_delay(self.personal_statement_input, personal_statement)
            self.click_element(self.next_button, delay=10)
        else:
            print("Personal Statement section is already complete, proceeding to next section")