import time

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
    assert page.get_by_test_id("login-submit").is_disabled()
    assert page.get_by_test_id("login-submit-text").is_hidden()
    assert page.get_by_test_id("login-submit-spinner").is_visible()

    page.get_by_test_id("login-submit-spinner").wait_for(state="hidden")
    assert page.get_by_test_id("login-submit").is_enabled()
    assert page.get_by_test_id("login-submit-spinner").is_hidden()
    assert page.get_by_test_id("login-submit-text").is_visible()

    timeout = 5.0
    step = 0.2
    elapsed = 0.0
    current_text = ""

    while elapsed < timeout:
        current_text = error_locator.inner_text().strip()
        if current_text:
            break
        time.sleep(step)
        elapsed += step

    assert current_text == "Invalid login or password.", (
        f"Текст ошибки не совпал. Ожидали: 'Invalid login or password.', получено: '{current_text}'"
    )
