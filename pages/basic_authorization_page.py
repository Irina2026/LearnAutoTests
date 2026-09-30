from playwright.sync_api import Page

from pages.base_page import BasePage
from ui import WebElement


class BasicAuthorization(BasePage):
    PATH = "/basic_auth"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.success_text = WebElement(page=page, locator=
            self.page.locator(".example p"),  # Всего один example, иначе #content .example p
            # (параграф внутри .example внутри #content)
            description="Basic Auth -> Success message",  # Висячая запятая, чистый diff(разница), если аргументы
            # в одну строку, то не ставить
        )

    def get_success_text(self) -> str:
        return self.success_text.get_inner_text()