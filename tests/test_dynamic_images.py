from playwright.sync_api import Page

from pages.dynamic_images_page import DynamicImagesPage


def test_dynamic_content(managed_page: Page):
    managed_page.goto("/dynamic_content")
    page = DynamicImagesPage(managed_page)

    matched = page.refresh_until_duplicate() # если не найдено, тест упадет здесь

    assert page.get_srcs().count(matched) >= 2 # если найдено - доп проверка