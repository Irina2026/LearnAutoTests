from playwright.sync_api import Page
from pages.alerts_page import AlertsPage
from faker import Faker

faker = Faker()

def test_alerts_page(managed_page: Page):

    text = faker.word()  # если текст длинный, тест падает, возможно ограничение на длину строки

    alerts_page = AlertsPage(managed_page)
    alerts_page.open()

    assert alerts_page.check_text_alert_button() == "I am a JS Alert"
    assert alerts_page.check_result_alert_button() == "You successfully clicked an alert"

    assert alerts_page.check_text_confirm_button() == "I am a JS Confirm"
    assert alerts_page.check_result_confirm_button() == "You clicked: Ok"

    assert alerts_page.check_text_prompt_button() == "I am a JS prompt"
    assert alerts_page.fill_and_check_result_prompt(text) == f"You entered: {text}"