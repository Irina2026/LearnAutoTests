import random

from playwright.sync_api import Page
import pytest
from pages.slider_page import SliderPage


def test_slider_page(managed_page: Page):
    count = random.randint(1, 9)
    slider_page = SliderPage(managed_page)
    slider_page.open()

    actual_text = slider_page.focus_slider_and_use_arrow_key("ArrowRight", count)
    actual_value = float(actual_text)

    expected_value = count * slider_page.get_step()

    assert actual_value == pytest.approx(expected_value), (
        f"count={count}, отображается '{actual_text}'"
    )
