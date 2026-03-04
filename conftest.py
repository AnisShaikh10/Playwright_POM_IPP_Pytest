from utils.data_generator import generate_user, generate_residence_details, generate_random_paragraph
from playwright.sync_api import sync_playwright
import pytest, os
from datetime import datetime

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
        page.close()
        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks first
    outcome = yield
    report = outcome.get_result()

    # We only care about actual test call failures
    if report.when == "call" and report.failed:

        # Check if test uses the page fixture
        page = item.funcargs.get("page", None)

        if page:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            file_path = os.path.join(
                screenshots_dir,
                f"{test_name}_{timestamp}.png"
            )

            page.screenshot(path=file_path)
            print(f"\n📸 Screenshot saved to: {file_path}")