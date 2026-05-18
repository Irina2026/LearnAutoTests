from playwright.sync_api import Page

from core.base_page import BasePage
from pages.search_results_page import SearchResultsPage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._search_input = page.get_by_test_id("search-input")
        self._search_button = page.get_by_test_id("search-button")

    def search(self, article_name):
        self._search_input.fill(article_name)
        self._search_button.click()

        return SearchResultsPage(self.page)
