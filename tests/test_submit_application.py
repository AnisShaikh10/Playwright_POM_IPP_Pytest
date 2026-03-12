import pytest
from pages.create_user import CreateUserPage
from pages.account_verification import AccountVerificationPage
from pages.login_page import LoginPage
from pages.personal_details_page import PersonalDetailsPage
from pages.contact_details_page import ContactDetailsPage
from pages.passport_and_residency_details_page import PassportAndResidencyDetailsPage
from pages.agent_details_page import AgentDetailsPage
from pages.qualification_page import QualificationsPage
from pages.english_proficiency_page import EnglishProficiencyPage
from pages.personal_statement_page import PersonalStatementPage
from pages.programme_related_information_page import ProgrammeRelatedInformationPage
from pages.experience_page import ExperiencePage
from pages.research_page import ResearchPage
from pages.reference_page import ReferencePage
from pages.additional_information_page import AdditionalInformationPage
from pages.submit_application_page import SubmitApplicationPage

login_url = "Your Login URL"

ipp_link_url = (
    "Your IPP Link URL"
)

def complete_application_flow(page, residence_details, text_statement):
    personal_details_page = PersonalDetailsPage(page)
    personal_details_page.edit_personal_details()

    contact_details_page = ContactDetailsPage(page)
    contact_details_page.edit_contact_details(residence_details)

    passport_and_residency_details_page = PassportAndResidencyDetailsPage(page, residence_details)
    passport_and_residency_details_page.edit_passport_and_residency_details(residence_details)

    agent_details_page = AgentDetailsPage(page)
    agent_details_page.edit_agent_details()

    qualification_details_page = QualificationsPage(page)
    qualification_details_page.edit_qualification_details()

    english_proficiency_page = EnglishProficiencyPage(page)
    english_proficiency_page.edit_english_proficiency()

    personal_statement_page = PersonalStatementPage(page)
    personal_statement_page.edit_personal_statement(text_statement)

    programme_related_information_page = ProgrammeRelatedInformationPage(page)
    programme_related_information_page.edit_programme_related_information()

    experience_page = ExperiencePage(page)
    experience_page.edit_experience()

    research_page = ResearchPage(page)
    research_page.edit_research(text_statement)

    reference_page = ReferencePage(page, residence_details)
    reference_page.edit_reference(residence_details)

    additional_information_page = AdditionalInformationPage(page)
    additional_information_page.edit_additional_information()
    
    submit_application_page = SubmitApplicationPage(page)
    submit_application_page.submit_application()

@pytest.mark.parametrize("user_data", ["H"], indirect=True)  # 👈 passing fee status here
def test_submit_application(page, user_data, residence_details, text_statement):
    # Create user and fill personal details
    create_user_page = CreateUserPage(page)
    create_user_page.navigate_to_ipp_link(url=ipp_link_url)
    create_user_page.fill_user_details(user_data)
    create_user_page.submit_form()
    create_user_page.expect_success_message()
    create_user_page.continue_application()

    # Verify account and proceed to personal details
    account_verification_page = AccountVerificationPage(page)
    account_verification_page.verify_account()
    
    try:
        complete_application_flow(page, residence_details, text_statement)
    except Exception as e:
        print("⚠ Form filling failed. Retrying via login...")
        # Login
        login_page = LoginPage(page)
        login_page.navigate_to_login_page(url=login_url)
        login_page.fill_login_details(username=user_data.email, password="Infuse@12345")
        login_page.verify_login_successful()
        # Retry flow
        complete_application_flow(page, residence_details, text_statement)
