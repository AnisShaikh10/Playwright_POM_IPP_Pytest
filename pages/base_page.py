from playwright.sync_api import Page, expect, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def click_element(self, target, by: dict = None, exact: bool = False, delay: int = 0, **kwargs):
        loc = target if isinstance(target, Locator) else self.page.locator(target)
        if by:
            if by.get("role") and by.get("name"):
                loc = loc.get_by_role(by["role"], name=by["name"], exact=exact)
            elif by.get("label"):
                loc = loc.get_by_label(by["label"], exact=exact)
            elif by.get("text"):
                loc = loc.get_by_text(by["text"], exact=exact)
            elif by.get("placeholder"):
                loc = loc.get_by_placeholder(by["placeholder"], exact=exact)

        if delay:
            self.page.wait_for_timeout(delay)

        loc.click(**kwargs)

    # Generic double‑click (supports locator or string)
    def double_click_element(self, target,by: dict = None, exact: bool = False, delay: int = 0, **kwargs):
        loc = target if isinstance(target, Locator) else self.page.locator(target)
        if by:
            if by.get("role") and by.get("name"):
                loc = loc.get_by_role(by["role"], name=by["name"], exact=exact)
            elif by.get("label"):
                loc = loc.get_by_label(by["label"], exact=exact)
            elif by.get("text"):
                loc = loc.get_by_text(by["text"], exact=exact)
            elif by.get("placeholder"):
                loc = loc.get_by_placeholder(by["placeholder"], exact=exact)

        if delay:
            self.page.wait_for_timeout(delay)

        loc.dblclick(**kwargs)

    # Generic fill (supports locator or string)
    def fill_input(self, target, value: str):
        if isinstance(target, Locator):
            target.fill(value)
        else:
            self.page.fill(target, value)

    # Generic fill (supports locator or string) WITH DELAY
    def fill_input_with_delay(self, target, value: str, delay: int = 10):
        if isinstance(target, Locator):
            target.click()
            target.type(value, delay=delay)
        else:
            locator = self.page.locator(target)
            locator.click()
            locator.clear()
            locator.type(value, delay=delay)
    
    def select_option(self, target, value):
        locator = target if isinstance(target, Locator) else self.page.locator(target)
        if isinstance(value, str):
            locator.select_option(value=value)
            return
        locator.select_option(value)

    # Expectation (supports locator or string)
    def is_element_visible(self, target):
        try:
            if isinstance(target, Locator):
                expect(target).to_be_visible()
            else:
                expect(self.page.locator(target)).to_be_visible()
            return True
        except Exception:
            return False
    
    def assert_element_is_visible(self, target):
        locator = target if isinstance(target, Locator) else self.page.locator(target)
        expect(locator).to_be_visible()

    # Wait for element (supports locator or string)
    def wait_for_element(self, target, timeout=30000):
        if isinstance(target, Locator):
            target.wait_for(state="visible", timeout=timeout)
        else:
            self.page.wait_for_selector(target, state="visible", timeout=timeout)