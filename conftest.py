from utils.data_generator import generate_user, generate_residence_details, generate_random_paragraph
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture
def user_data(request):
    fee_status = request.param
    user = generate_user(fee_status)
    print("User data:", user)
    return user

@pytest.fixture
def residence_details(user_data):
    return generate_residence_details(user_data.country)

@pytest.fixture
def text_statement():
    return generate_random_paragraph()

@pytest.fixture
def page():
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False, slow_mo=300, args = ["--start-maximized"])
        browser = p.chromium.launch(headless=False, args = ["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()