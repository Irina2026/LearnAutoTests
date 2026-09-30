from playwright.sync_api import Page

from pages.context_page import ContextPage


def test_context_page(managed_page: Page):
    context_page = ContextPage(managed_page)
    context_page.open()
    assert context_page.right_click_and_accept_alert() == "You selected a context menu"
