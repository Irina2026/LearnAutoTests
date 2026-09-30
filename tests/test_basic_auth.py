from playwright.sync_api import Page
from pages.basic_authorization_page import BasicAuthorization

def test_basic_auth(managed_page_with_auth: Page):

    auth_page = BasicAuthorization(managed_page_with_auth)
    auth_page.open()

    assert auth_page.get_success_text() == "Congratulations! You must have the proper credentials."
