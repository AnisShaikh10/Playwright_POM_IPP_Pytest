from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.data_generator import ResidenceDetails
import time

class ReferencePage(BasePage):
    def __init__(self, page: Page, residence_details: ResidenceDetails):
        super().__init__(page)
        self.residence_details = residence_details

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Reference']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_reference_button(self):
        return self.page.get_by_role("link", name="Edit Referees")

    @property
    def reference_upload_dropdown(self):
        return self.page.get_by_label("Do you have a reference to")
    
    @property
    def reference_type_dropdown(self):
        return self.page.get_by_label("Type of reference*")
    
    @property
    def reference_name_input(self):
        return self.page.get_by_role("textbox", name="Name*")
    
    @property
    def reference_relationship_input(self):
        return self.page.get_by_role("textbox", name="Relationship to you?*")
    
    @property
    def position_input(self):
        return self.page.get_by_role("textbox", name="Position*")
    
    @property
    def reference_institution_input(self):
        return self.page.get_by_role("textbox", name="Institution/company*")
    
    @property
    def country_dropdown(self):
        return self.page.locator("a").filter(has_text="Please Select")
    
    @property
    def country_options(self):
        return self.page.get_by_role("option", name=self.residence_details.country_of_residence)
    
    @property
    def postal_code_input(self):
        return self.page.get_by_role("textbox", name="Postal/zip code*")
    
    @property
    def address_line1_input(self):
        return self.page.get_by_role("textbox", name="Address line 1*")
    
    @property
    def email_address_input(self):
        return self.page.get_by_role("textbox", name="Email address*")
    
    @property
    def referee2_header(self):
        return self.page.get_by_role("heading", name="Referee 2")

    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    
    def edit_reference(self, refree_details : ResidenceDetails):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_reference_button)
            time.sleep(1)
            self.select_option(self.reference_upload_dropdown, "No")
            self.select_option(self.reference_type_dropdown, "Academic")
            self.fill_input_with_delay(self.reference_name_input, "Test Referee Name", delay=1)
            self.fill_input(self.reference_relationship_input, "Test Relationship")
            self.fill_input(self.position_input, "Test Position")
            self.fill_input(self.reference_institution_input, "Test Institution")
            self.click_element(self.country_dropdown)
            self.click_element(self.country_options)
            self.fill_input(self.postal_code_input, refree_details.postal_code)
            self.fill_input(self.address_line1_input, refree_details.address_line1)
            self.fill_input(self.email_address_input, "UniversityTest@mailinator.com")
            self.click_element(self.next_button)
            second_referee = self.is_element_visible(self.referee2_header)
            if second_referee:
                print("Filling details for second referee")
                self.select_option(self.reference_upload_dropdown, "No")
                self.select_option(self.reference_type_dropdown, "Academic")
                self.fill_input_with_delay(self.reference_name_input, "Test Referee Name 2", delay=1)
                self.fill_input(self.reference_relationship_input, "Test Relationship 2")
                self.fill_input(self.position_input, "Test Position 2")
                self.fill_input(self.reference_institution_input, "Test Institution 2")
                self.click_element(self.country_dropdown)
                self.click_element(self.country_options)
                self.fill_input(self.postal_code_input, refree_details.postal_code)
                self.fill_input(self.address_line1_input, refree_details.address_line1)
                self.fill_input(self.email_address_input, "UniversityTest2@mailinator.com")
                self.click_element(self.next_button)
        else:
            print("Reference section is already complete, proceeding to next section")