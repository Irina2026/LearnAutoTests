from playwright.sync_api import Page

from pages.base_page import BasePage
from ui import WebElement


class AlertsPage(BasePage):
    PATH = "/javascript_alerts"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.js_alert_button = WebElement(page=page,
                                          locator=self.page.get_by_role("button", name="Click for JS Alert"),
                                          description="Click for JS Alert",
                                          )


        self.js_confirm_button = WebElement(page=page,
                                            locator=self.page.get_by_role("button", name="Click for JS Confirm"),
                                            description="Click for JS Confirm",
                                            )

        self.js_prompt_button = WebElement(page=page,
                                           locator=self.page.get_by_role("button", name="Click for JS Prompt"),
                                           description="Click for JS Prompt",
                                           )

        self.result = WebElement(page=page,
                                 locator=self.page.locator("#result"),
                                 description="Result text",
                                 )


    def check_text_alert_button(self) -> str:
        return self.page_actions.run_and_accept_alert(self.js_alert_button.click)

    def check_result_alert_button(self) -> str:
         self.page_actions.run_and_accept_alert(self.js_alert_button.click)
         return self.result.get_inner_text()

    def check_text_confirm_button(self) -> str:
        return self.page_actions.run_and_accept_alert(self.js_confirm_button.click)

    def check_result_confirm_button(self) -> str:
        self.page_actions.run_and_accept_alert(self.js_confirm_button.click)
        return self.result.get_inner_text()

    def check_text_prompt_button(self) -> str:
        return self.page_actions.run_and_accept_alert(self.js_prompt_button.click)

    def fill_and_check_result_prompt(self, text: str) -> str:
        self.page_actions.run_and_accept_prompt(self.js_prompt_button.click, text)
        return self.result.get_inner_text()