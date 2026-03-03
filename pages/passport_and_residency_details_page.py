from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.data_generator import ResidenceDetails

class PassportAndResidencyDetailsPage(BasePage):
    def __init__(self, page: Page, residence_details: ResidenceDetails):
        super().__init__(page)
        self.residence_details = residence_details

    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Passport and Residency Details']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_passport_and_residency_details_button(self):
        return self.page.get_by_role("link", name="Edit Identity/Passport Details")

    @property
    def country_dropdown(self):
        return self.page.locator("a").filter(has_text="Please select the country in")
    
    @property
    def country_options(self):
        return self.page.get_by_role("option", name=self.residence_details.address_country)
    
    @property
    def legal_nationality_dropdown(self):
        return self.page.locator("//label[text()=' Legal nationality (as on passport)* ']/following::div[2]")
    
    @property
    def legal_nationality_option_input(self):
        return self.page.get_by_role("textbox", name="Legal nationality (as on passport)")

    @property
    def legal_nationality_options(self):
        return self.page.get_by_role("option", name=self.residence_details.legal_nationality)
    
    @property
    def passport_number_input(self):
        return self.page.locator("(//label[text()=' Passport number ']/following::input[1])[1]")
    
    @property
    def date_of_issue_date(self):
        return self.page.locator("(//label[text()='Date']/child::span[text()='Date of issue']/following::select[1])[1]")
    
    @property
    def date_of_issue_month(self):
        return self.page.locator("(//label[text()='Month']/child::span[text()='Date of issue']/following::select[1])[1]")
    
    @property
    def date_of_issue_year(self):
        return self.page.locator("(//label[text()='Year']/child::span[text()='Date of issue']/following::select[1])[1]")
    
    @property
    def date_of_expiry_date(self):
        return self.page.locator("(//label[text()='Date']/child::span[text()='Date of expiry']/following::select[1])[1]")
    
    @property
    def date_of_expiry_month(self):
        return self.page.locator("(//label[text()='Month']/child::span[text()='Date of expiry']/following::select[1])[1]")
    
    @property
    def date_of_expiry_year(self):
        return self.page.locator("(//label[text()='Year']/child::span[text()='Date of expiry']/following::select[1])[1]")
    
    @property
    def country_of_residence_dropdown(self):
        return self.page.locator("//label[text()=' Country of residence* ']/following::div[1]")
    
    @property
    def country_of_residence_options(self):
        return self.page.get_by_label("Country of residence* options").get_by_role("option", name=self.residence_details.country_of_residence)
    
    @property
    def residential_category_dropdown(self):
        return self.page.locator("//label[contains(text(),'residential category')]/following::select[1]")
    
    @property
    def euss_status_dropdown(self):
        return self.page.get_by_label("Do you have EUSS settled or")
    
    @property
    def study_visa_dropdown(self):
        return self.page.get_by_label("Do you require a student visa")
    
    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    
    def edit_passport_and_residency_details(self, contact_details: ResidenceDetails):
        is_section_incomplete = self.is_element_visible(self.form_incomplete_sign)
        if is_section_incomplete:
            self.click_element(self.edit_passport_and_residency_details_button)
            self.click_element(self.country_dropdown)
            self.click_element(self.country_options)
            self.click_element(self.legal_nationality_dropdown)
            self.fill_input(self.legal_nationality_option_input, contact_details.legal_nationality)
            self.click_element(self.legal_nationality_options)
            self.fill_input(self.passport_number_input, contact_details.passport_number)
            self.select_option(self.date_of_issue_date, "01")
            self.select_option(self.date_of_issue_month, "01")
            self.select_option(self.date_of_issue_year, "2020")
            self.select_option(self.date_of_expiry_date, "01")
            self.select_option(self.date_of_expiry_month, "01")
            self.select_option(self.date_of_expiry_year, "2030")
            self.click_element(self.country_of_residence_dropdown)
            self.click_element(self.country_of_residence_options)
            self.select_option(self.residential_category_dropdown, contact_details.residential_category)
            self.select_option(self.euss_status_dropdown, "No")
            self.select_option(self.study_visa_dropdown, contact_details.require_student_visa)
            self.click_element(self.next_button)
        else:
            print("Passport and residency details section is already complete, proceeding to next section")