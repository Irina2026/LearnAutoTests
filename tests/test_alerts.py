from faker import Faker
from playwright.sync_api import Page

from pages.alerts_page import AlertsPage

faker = Faker()


def test_alerts_page(managed_page: Page):
    text = faker.word()  # если текст длинный, тест падает, возможно ограничение на длину строки

    managed_page.goto("/javascript_alerts")

    alerts_page = AlertsPage(managed_page)

    actual_text_alert = alerts_page.check_text_alert_button()
    assert actual_text_alert == "I am a JS Alert", (
        f"Ожидалось: 'I am a JS Alert', получено: '{actual_text_alert}'"
    )

    actual_result_alert = alerts_page.check_result_alert_button()
    assert actual_result_alert == "You successfully clicked an alert", (
        f"Ожидалось: 'You successfully clicked an alert', получено: '{actual_result_alert}'"
    )

    actual_text_confirm = alerts_page.check_text_confirm_button()
    assert actual_text_confirm == "I am a JS Confirm", (
        f"Ожидалось: 'I am a JS Confirm', получено: '{actual_text_confirm}'"
    )

    actual_result_confirm = alerts_page.check_result_confirm_button()
    assert actual_result_confirm == "You clicked: Ok", (
        f"Ожидалось: 'You clicked: Ok', получено: '{actual_result_confirm}'"
    )

    actual_text_prompt = alerts_page.check_text_prompt_button()
    assert actual_text_prompt == "I am a JS prompt", (
        f"Ожидалось: 'I am a JS prompt', получено: '{actual_text_prompt}'"
    )

    actual_result_prompt = alerts_page.fill_and_check_result_prompt(text)
    expected_result_prompt = f"You entered: {text}"
    assert actual_result_prompt == expected_result_prompt, (
        f"Ожидалось: '{expected_result_prompt}', получено: '{actual_result_prompt}'"
    )