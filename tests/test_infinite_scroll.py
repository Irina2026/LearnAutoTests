from playwright.sync_api import Page

from pages.infinite_scroll_page import InfiniteScrollPage


def test_infinite_scroll(managed_page: Page):

    managed_page.goto("/infinite_scroll")

    page = InfiniteScrollPage(managed_page)


    page.scroll_until_at_least(10)

    assert page.get_count() >= 10