from playwright.sync_api import Page

from core.base_page import BasePage
from pages.search_results_page import SearchResultsPage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        home_selectors = self.config.selectors.get("home", {})
        self._search_input = page.locator(home_selectors.get("search_input", ""))
        self._search_button = page.locator(home_selectors.get("search_button", ""))
        self._results_container = page.locator(
            self.config.selectors.get("results", {}).get("results_container", ""))

    def search(self, article_name):
        name = article_name or self.config.search.get("default_article_name")
        self._search_input.fill(name)
        self._search_button.click()

        self._results_container.wait_for(state="visible")

        return SearchResultsPage(self.page)
