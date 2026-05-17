from playwright.sync_api import Page

from core.base_page import BasePage
from pages.search_results_page import SearchResultsPage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._search_input = page.get_by_test_id("search-input")
        self._search_button = page.get_by_test_id("search-button")
        self._results_container = page.get_by_test_id("search-results-section")

    def search(self, article_name):
        name = article_name
        self._search_input.fill(name)
        self._search_button.click()

        self._results_container.wait_for(state="visible")

        return SearchResultsPage(self.page)
