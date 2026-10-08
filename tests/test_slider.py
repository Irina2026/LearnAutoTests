import random

import pytest
from playwright.sync_api import Page

from pages.slider_page import SliderPage

"""
в headed-режиме тест зелёный, а в headless красный — это Chromium-специфика, запускать отдельно или 
узнать, как обходить эту особенность
"""


def test_slider_page(managed_page: Page):
    managed_page.goto("/horizontal_slider")
    slider_page = SliderPage(managed_page)

    min_value = slider_page.get_min()
    max_value = slider_page.get_max()
    step = slider_page.get_step()

    max_steps = int(round((max_value - min_value) / step))
    count = random.randint(1, max_steps)
    target_value = min_value + count * step

    actual_text = slider_page.set_value(target_value)
    actual_value = float(actual_text)

    assert actual_value == pytest.approx(target_value), (
        f"Ожидалось: '{target_value}', получено: '{actual_text}'"
    )