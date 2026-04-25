from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()
fake.seed_instance(42)
BASE_URL = "http://144.31.139.115:5000/"


def test_login_page(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Article Store")
    page.get_by_role("link", name="Login").click()
    expect(page).to_have_title("Login")
    page.get_by_role("textbox", name="Login").fill(fake.word())
    page.get_by_role("textbox", name="Password").fill(fake.word())
    page.get_by_role("button", name="Confirm").click()
    expect(page.get_by_test_id("login-submit")).to_be_disabled()
    expect(page.get_by_test_id("login-submit-text")).to_be_hidden()
    expect(page.get_by_test_id("login-submit-spinner")).to_be_visible()
    expect(page.get_by_test_id("login-submit")).to_be_enabled()
    expect(page.get_by_test_id("login-submit-spinner")).to_be_hidden()
    expect(page.get_by_test_id("login-submit-text")).to_be_visible()
    expect(page.get_by_text("Invalid login or password.")).to_be_visible()
