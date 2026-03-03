from playwright.sync_api import Page
from pages.base_page import BasePage

class AdditionalInformationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Additional Information']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_additional_information_button(self):
        return self.page.get_by_role("row", name="Additional Information ").get_by_role("link")

    @property
    def ethnic_group_dropdown(self):
        return self.page.get_by_label("What is your ethnicity or")
    
    @property
    def ciminal_conviction_dropdown(self):
        return self.page.get_by_label("Do you have any unspent criminal convictions?")
    
    @property
    def disability_dropdown(self):
        return self.page.get_by_label("Do you wish to declare any")
    
    @property
    def incare_dropdown(self):
        return self.page.get_by_label("Have you been in care?")
    
    @property
    def estranged_dropdown(self):
        return self.page.get_by_label("Would you consider yourself")
    
    @property
    def funding_information_check(self):
        return self.page.get_by_text("Self Funding")
    
    @property
    def find_about_course(self):
        return self.page.get_by_label("How Did You Find Out About")
    
    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    def edit_additional_information(self):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_additional_information_button)
            self.select_option(self.ethnic_group_dropdown, "Prefer not to say")
            criminal_conviction_visible = self.is_element_visible(self.ciminal_conviction_dropdown)
            if criminal_conviction_visible:
                self.select_option(self.ciminal_conviction_dropdown, "N")
            self.select_option(self.disability_dropdown, "Prefer not to say")
            self.select_option(self.incare_dropdown, "Not known")
            self.select_option(self.estranged_dropdown, "Information refused")
            self.click_element(self.next_button)
            self.click_element(self.funding_information_check)
            self.click_element(self.next_button)
            self.select_option(self.find_about_course, "Social media")
            self.click_element(self.next_button)
        else:
            print("Additional Information section is already complete, proceeding to next section")