from decimal import Decimal

from playwright.sync_api import Page

from core.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._filter_dropdown = page.get_by_test_id("filter-sort")
        self._results_loader = page.get_by_test_id("results-loader")
        self._results_container = page.get_by_test_id("search-results-section")
        self._price_element = self._results_container.locator('[data-price]')

    def apply_filter(self, filter_type):
        self._filter_dropdown.select_option(value=filter_type)
        self._results_loader.wait_for(state="visible")
        self._results_loader.wait_for(state="hidden")
        self._results_container.wait_for(state="visible")
        self.page.wait_for_load_state(state="domcontentloaded")

    def get_prices(self, count: int):
        self._price_element.first.wait_for(state="attached")
        prices = []
        elements = self._price_element.all()

        for el in elements[:count]:
            raw = el.get_attribute("data-price")
            if raw:
                prices.append(Decimal(raw))

        return prices
