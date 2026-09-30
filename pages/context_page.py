from playwright.sync_api import Page

from pages.base_page import BasePage
from ui import WebElement


class ContextPage(BasePage):
    PATH = "/context_menu"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.context_button = WebElement(page=page,
                                         locator=self.page.locator("#hot-spot"),
                                         description="Context menu",
                                         )

    def right_click_and_accept_alert(self) -> str:
        return self.page_actions.run_and_accept_alert(self.context_button.right_click)
