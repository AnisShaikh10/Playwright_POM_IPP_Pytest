from playwright.sync_api import Page
from pages.base_page import BasePage

class ResearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def research_section_header(self):
        return self.page.get_by_role("cell", name="Research", exact=True)
    
    @property
    def form_incomplete_sign(self):
        return self.page.locator("//span[text()='Research']/parent::td"
        "/following-sibling::td//b[text()='Status']/following-sibling::span/span[text()='Graphic Cross item incomplete']")
    
    @property
    def edit_research_button(self):
        return self.page.get_by_role("link", name="Edit Research Proposal")

    @property
    def project_title(self):
        return self.page.get_by_role("textbox", name="Proposed project title/")
    
    @property
    def proposed_supervisor(self):
        return self.page.get_by_label("Proposed supervisor")
    
    @property
    def studentship_code(self):
        return self.page.get_by_label("Studentship Code*")
    
    @property
    def research_upload_dropdown(self):
        return self.page.get_by_label("Do you have a research")
    
    @property
    def research_proposal_input(self):
        return self.page.get_by_role("textbox", name="Please instead type your")

    @property
    def next_button(self):
        return self.page.get_by_role("button", name="Next")
    
    def edit_research(self, research_proposal):
        # Wait for research section to be visible
        if not self.is_element_visible(self.research_section_header):
            print("Research section not visible, skipping...")
            return

        # Check if section is incomplete
        if not self.is_element_visible(self.form_incomplete_sign):
            print("Research section already complete, skipping...")
            return

        # Click edit
        self.click_element(self.edit_research_button)
        # Wait for form fields to be ready
        self.wait_for_element(self.project_title)
        # Fill details
        self.fill_input(self.project_title, "Test Project Title")
        self.select_option(self.proposed_supervisor, "Auto Testing")
        self.select_option(self.studentship_code, "0 NOT APPLICABLE")
        self.select_option(self.research_upload_dropdown, "No")
        self.fill_input(self.research_proposal_input, research_proposal)
        self.click_element(self.next_button)