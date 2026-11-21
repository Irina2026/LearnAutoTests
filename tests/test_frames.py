from playwright.sync_api import Page
from pages.frames_page import FramesPage


def test_nested_frames(managed_page: Page):
    managed_page.goto("/nested_frames")
    frames = FramesPage(managed_page)

    assert frames.get_left_text() == "LEFT", "Неверный текст в левом фрейме"

    assert frames.get_right_text() == "RIGHT", "Неверный текст в правом фрейме"

    assert frames.get_bottom_text() == "BOTTOM", "Неверный текст в нижнем фрейме"

    assert frames.get_middle_text() == "MIDDLE", "Неверный текст в центральном фрейме"
