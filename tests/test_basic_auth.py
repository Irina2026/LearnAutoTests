from playwright.sync_api import Page

from pages.basic_authorization_page import BasicAuthorization


def test_basic_auth(managed_page_with_auth: Page):
    managed_page_with_auth.goto("/basic_auth")
    auth_page = BasicAuthorization(managed_page_with_auth)

    actual_text = auth_page.get_success_text()
    expected_text = "Congratulations! You must have the proper credentials."
    assert actual_text == expected_text, (
        f"Ожидалось: '{expected_text}', получено: '{actual_text}'"
    )