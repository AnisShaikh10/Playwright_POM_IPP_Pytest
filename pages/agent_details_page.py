from playwright.sync_api import Page
from pages.base_page import BasePage


class AgentDetailsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Agent Details']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_agent_details_button(self):
        return self.page.get_by_role("link", name="Edit Agent Details")

    @property
    def confirm_agent(self):
        return self.page.get_by_text("I confirm that the person")
    
    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    
    def edit_agent_details(self):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_agent_details_button)
            self.click_element(self.next_button)
            locators = self.is_element_visible(self.confirm_agent)
            if locators:
                self.click_element(self.confirm_agent)
            self.click_element(self.next_button)
        else:
            print("Agent details section is already complete, proceeding to next section")