from playwright.sync_api import Page

from core.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        result_selectors = self.config.selectors.get("results", {})
        self._filter_dropdown = page.locator(result_selectors.get("filter_dropdown", ""))
        self._results_loader = page.locator(result_selectors.get("results_loader", ""))
        self._results_container = page.locator(result_selectors.get("results_container", ""))
        self._article_cards = page.locator(result_selectors.get("article_cards", ""))
        self._price_element = page.locator(result_selectors.get("price_element", ""))

    def apply_filter(self, filter_type):
        value = filter_type or self.config.search.get("default_filter_type")
        self._filter_dropdown.select_option(value=value)
        self._results_loader.wait_for(state="visible")
        self._results_loader.wait_for(state="hidden")
        self._results_container.wait_for(state="visible")
        return self

    def get_prices(self, count):

        c = count or self.config.search.get("default_results_count")

        raw_prices = self._price_element.evaluate_all(
            "els => els.map(el => el.getAttribute('data-price'))"
        )

        prices = []
        for price_str in raw_prices[:c]:
            if price_str:
                try:
                    prices.append(float(price_str) / 100)
                except ValueError:
                    continue
        return prices

    @staticmethod
    def is_sorted_ascending(prices):
        return sorted(prices) == prices

    @staticmethod
    def is_sorted_descending(prices):
        return sorted(prices, reverse=True) == prices

    def verify_sorted(self, filter_type, count):
        self.apply_filter(filter_type)
        prices = self.get_prices(count)
        filter_value = filter_type or self.config.search.get("default_filter_type")

        if filter_value == "price_asc":
            return self.is_sorted_ascending(prices)
        elif filter_value == "price_desc":
            return self.is_sorted_descending(prices)
        elif filter_value == "relevance":
            return True
        else:
            return False

