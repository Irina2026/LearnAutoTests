from playwright.sync_api import Page

from conftest import managed_page
from pages.hovers_page import HoversPage


def test_hovers(managed_page: Page):
    managed_page.goto("/hovers")
    hovers_page = HoversPage(managed_page)
    total = hovers_page.get_count()
    assert total > 0, "Карточки пользователей не найдены"

    for i in range(total):
        # До наведения имени не видно
        assert not hovers_page.is_caption_visible(i), (
            f"Подпись карточки {i} видна без hover"
        )

        # Наводим мышку на аватарку
        hovers_page.hover_avatar(i)

        # После наведения — видна
        assert hovers_page.is_caption_visible(i), (
            f"Подпись карточки {i} не появилась после hover"
        )

        # Проверяем имя
        actual = hovers_page.get_name(i)
        expected = f"name: user{i + 1}"
        assert actual == expected, (
            f"Карточка {i}: ожидали '{expected}', получили '{actual}'"
        )
