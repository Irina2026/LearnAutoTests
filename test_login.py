from faker import Faker
from playwright.sync_api import Page

fake = Faker()
BASE_URL = "http://144.31.139.115:5000/"


def test_login_page(page: Page):

    error_locator = page.get_by_test_id("login-error-inline")

    page.goto(BASE_URL)
    page.get_by_test_id("nav-login").click()

    page.get_by_test_id("login-title")
    page.get_by_test_id("login-username").fill(fake.word())
    page.get_by_test_id("login-password").fill(fake.word())

    page.get_by_test_id("login-submit").click()

    page.get_by_test_id("login-submit-spinner").wait_for(state="visible")
    page.get_by_test_id("login-submit-spinner").wait_for(state="hidden")

    error_text = error_locator.inner_text()

    assert "Invalid login or password." in error_text, f"Не нашли текст. Получено: {error_text}."
