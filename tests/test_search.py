import pytest
from playwright.sync_api import Page

from core.sorting_filters import FilterType
from pages.home_page import HomePage
from utils.sorting import is_sorted_ascending, is_sorted_descending

SEARCH_NAMES = ["city", "habits"]
SEARCH_COUNTS = [10, 15]

FILTER_VALUES = [FilterType.ASC, FilterType.DESC]


@pytest.mark.parametrize("filter_value", FILTER_VALUES)
@pytest.mark.parametrize("count", SEARCH_COUNTS)
@pytest.mark.parametrize("name", SEARCH_NAMES)
def test_search_with_custom_data(
        page: Page,
        base_url: str,
        name: str,
        count: int,
        filter_value: str
):
    page.goto(base_url)

    home = HomePage(page)
    results_page = home.search(name)

    results_page.apply_filter(filter_value)

    prices = results_page.get_prices(count)

    assert len(prices) == count, f"Ожидалось {count} цен, получено {len(prices)}"

    if filter_value == FilterType.ASC:
        assert is_sorted_ascending(prices), (
            f"Цены не отсортированы по возрастанию! Ожидалось {sorted(prices)}, получено: {prices}"
        )
    elif filter_value == FilterType.DESC:
        assert is_sorted_descending(prices), (
            f"Цены не отсортированы по убыванию! Ожидалось: {sorted(prices, reverse=True)}, получено: {prices}"
        )
