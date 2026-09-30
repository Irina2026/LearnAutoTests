from playwright.sync_api import Page

from ui import PageActions


class BasePage:
    """Базовый класс для всех страниц проекта."""

    PATH: str = ""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_actions = PageActions(page=page)

    def open(self) -> None:
        """Открывает страницу по пути, заданному в PATH наследника."""
        self.page_actions.goto(self.PATH)