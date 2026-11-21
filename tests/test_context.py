from playwright.sync_api import Page

from pages.context_page import ContextPage


def test_context_page(managed_page: Page):
    managed_page.goto("/context_menu")
    context_page = ContextPage(managed_page)

    actual_text = context_page.right_click_and_accept_alert()
    expected_text = "You selected a context menu"
    assert actual_text == expected_text, (
        f"Ожидалось: '{expected_text}', получено: '{actual_text}'"
    )