
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

# 📦 Таблица ваших данных → список кортежей
SEARCH_SCENARIOS = [
    ("city", 10, "price_asc"),  # Price: low to high
    ("city", 15, "price_desc"),  # Price: high to low
    ("habits", 10, "price_asc"),
    ("habits", 15, "price_desc"),
]


@pytest.mark.parametrize("name, count, filter_value", SEARCH_SCENARIOS)
def test_search_with_custom_data(
        page: Page,
        base_url: str,
        name: str,
        count: int,
        filter_value: str
):
    # 1. Открываем главную
    page.goto(base_url)

    # 2. Ищем статью по переданному `name`
    home = HomePage(page)
    results_page = home.search(name)  # ваш метод уже умеет принимать article_name

    # 3. Применяем фильтр (внутреннее значение value из <option>)
    results_page.apply_filter(filter_value)

    # 4. Получаем первые `count` цен
    prices = results_page.get_prices(count)

    # ✅ Проверка 1: вернулось ровно столько цен, сколько просили
    assert len(prices) == count, f"Ожидалось {count} цен, получено {len(prices)}"

    # ✅ Проверка 2: порядок соответствует фильтру
    if filter_value == "price_asc":
        assert results_page.is_sorted_ascending(prices), "Цены не отсортированы по возрастанию!"
    elif filter_value == "price_desc":
        assert results_page.is_sorted_descending(prices), "Цены не отсортированы по убыванию!"