from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.data_generator import ResidenceDetails

class ContactDetailsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Contact Details']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_contact_details_button(self):
        return self.page.get_by_role("link", name="Edit Contact Details")

    @property
    def country_dropdown(self):
        return self.page.get_by_label("Country*")
    
    @property
    def postcode_input(self):
        return self.page.get_by_role("textbox", name="Postal/Zip Code*")
    
    @property
    def address_line1_input(self):
        return self.page.get_by_role("textbox", name="Address Line 1*")
    
    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    @property
    def copy_address(self):
        return self.page.get_by_role("button", name="Copy Address")
    
    @property
    def available_addresses(self):
        return self.page.locator("#siwAddEditCopyList")
    
    @property
    def choose_copy_address(self):
        return self.page.get_by_label("Choose Address to Copy").get_by_role("button", name="Copy Address")
    
    @property
    def mobile_number_input(self):
        return self.page.get_by_role("textbox", name="Mobile*")
    
    def edit_contact_details(self, contact_details: ResidenceDetails):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_contact_details_button)
            self.select_option(self.country_dropdown, contact_details.country_of_residence)
            self.fill_input(self.postcode_input, contact_details.postal_code)
            self.fill_input(self.address_line1_input, contact_details.address_line1)
            self.click_element(self.next_button)
            self.click_element(self.copy_address)
            self.select_option(self.available_addresses, "0")
            self.click_element(self.choose_copy_address)
            self.click_element(self.next_button)
            self.fill_input(self.mobile_number_input, "07123456789")
            self.click_element(self.next_button)
        else:
            print("Contact details section is already complete, proceeding to next section")