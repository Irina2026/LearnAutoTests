from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    PATH = "/hovers"

    def __init__(self, page: Page):
        super().__init__(page)

        self.all_cards = MultiWebElement(page=page,
                                         locator=self.page.locator(".figure"),
                                         description="All cards",
                                         )

    def get_count(self) -> int:
        return self.all_cards.count()
