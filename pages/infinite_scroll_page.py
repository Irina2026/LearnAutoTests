from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from ui.web_element import WebElement
from ui.multi_web_element import MultiWebElement

class InfiniteScrollPage(BasePage):
    TARGET_COUNT = 10
    MAX_ATTEMPTS = 30

    def __init__(self, page: Page):
        super().__init__(page)
        self.scroll_container = WebElement(
            page=page,
            locator=page.locator(".scroll"),
            description="Scroll container",
        )
        self.paragraphs = MultiWebElement(
            page=page,
            locator=page.locator(".jscroll-added"),
            description="Paragraphs",
        )

    def get_count(self) -> int:
        return self.paragraphs.count()

    def scroll_until_at_least(self, target: int = TARGET_COUNT) -> None:
        for _ in range(self.MAX_ATTEMPTS):
            count = self.get_count()
            if count >= target:
                return

            self.scroll_container.hover()

            # Крутим колесо несколько раз — гарантированно доходим до низа документа
            for _ in range(10):
                self.page.mouse.wheel(0, 1000)

            expect(self.paragraphs.locator).not_to_have_count(count, timeout=5000)

        raise AssertionError(
            f"Не набрали {target} абзацев за {self.MAX_ATTEMPTS} попыток. "
            f"Сейчас: {self.get_count()}"
        )