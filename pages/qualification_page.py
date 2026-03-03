from playwright.sync_api import Page
from pages.base_page import BasePage
import time

class QualificationsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Qualifications']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_qualification_details_button(self):
        return self.page.get_by_role("link", name="Edit Qualifications")

    @property
    def highest_qualification(self):
        return self.page.get_by_label("What is the highest level of")
    
    @property
    def last_institution_attended(self):
        return self.page.get_by_role("textbox", name="What is the last institution")
    
    @property
    def option_results(self):
        return self.page.locator("#dmu_results_div")
    
    @property
    def add_qualification_button(self):
        return self.page.get_by_role("button", name="Add qualification")
    
    @property
    def institution_name(self):
        return self.page.get_by_role("textbox", name="Institution / school /")
    
    @property
    def qualification_type(self):
        return self.page.get_by_label("Type of qualification*")
    
    @property
    def qualification_name(self):
        return self.page.get_by_role("textbox", name="Qualification Name (for")
    
    @property
    def subject_name(self):
        return self.page.get_by_role("textbox", name="Subject name*")

    @property
    def subject_options(self):
        return self.page.get_by_role("option", name="Computer Applications")
    
    @property
    def completed(self):
        return self.page.get_by_label("Completed?*")
    
    @property
    def completion_date(self):
        return self.page.get_by_role("textbox", name="Completion / expected")

    @property
    def save_button(self):
        return self.page.get_by_role("button", name="Save")
    
    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    
    def edit_qualification_details(self):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_qualification_details_button)
            time.sleep(1)
            self.select_option(self.highest_qualification, "Foundation degree")
            self.fill_input_with_delay(self.last_institution_attended, "University of Plymouth", delay=10)
            self.click_element(self.option_results, delay=2000)
            self.click_element(self.add_qualification_button)
            self.fill_input_with_delay(self.institution_name, "City College Plymouth", delay=10)
            self.click_element(self.option_results, delay=2000)
            self.select_option(self.qualification_type, "ACAD")
            self.fill_input_with_delay(self.qualification_name, "Master's Degree", delay=100)
            self.double_click_element(self.option_results)
            self.fill_input_with_delay(self.subject_name, "Computer Applications", delay=10)
            self.click_element(self.subject_options)
            self.select_option(self.completed, "N")
            self.fill_input(self.completion_date, "10/Feb/2027")
            self.click_element(self.save_button, delay=2000)
            self.click_element(self.next_button, delay=5000)
        else:
            print("Qualification details section is already complete, proceeding to next section")