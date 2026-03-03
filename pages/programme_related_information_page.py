from playwright.sync_api import Page
from pages.base_page import BasePage

class ProgrammeRelatedInformationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def programme_related_info_header(self):
        return self.page.get_by_role("cell", name="Programme Related Information", exact=True)

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Programme Related Information']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_programme_related_information_button(self):
        return self.page.get_by_role("row", name="Programme Related Information").get_by_role("link")

    @property
    def programme_specialist(self):
        return self.page.get_by_role("textbox", name="Applicants can only study one")

    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    def edit_programme_related_information(self):
        # Wait for programme related information section to be visible
        if not self.is_element_visible(self.programme_related_info_header):
            print("Programme Related Information section not visible, skipping...")
            return

        # Check if section is incomplete
        if not self.is_element_visible(self.form_incomplete_sign):
            print("Programme Related Information section already complete, skipping...")
            return
        
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_programme_related_information_button)
            self.fill_input(self.programme_specialist, "Cancer Biology")
            self.click_element(self.next_button)
        else:
            print("Programme Related Information section is already complete, proceeding to next section")