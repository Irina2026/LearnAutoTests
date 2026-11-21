from playwright.sync_api import Page
from pages.base_page import BasePage

"""
Фрейм — это «окно внутри окна». В одном HTML-документе можно разместить другой HTML-документ. 
Визуально он выглядит как прямоугольная область внутри страницы, а по сути — отдельная страница, со своим DOM, своим 
<body>, своими элементами.
<iframe>	Современный, используется повсеместно	Может быть в любом месте <body>
<frame>	Устаревший (HTML4), но ещё работает	Только внутри <frameset> вместо <body>
"""


class FramesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Входные точки
        self.top_frame = page.frame_locator('frame[name="frame-top"]')  # при первом использовании найдёт фрейм и
        # направит поиск внутрь него
        self.bottom_frame = page.frame_locator('frame[name="frame-bottom"]')

    def get_left_text(self) -> str:
        return self._top_child_text("frame-left")

    def get_middle_text(self) -> str:
        return self._top_child_text("frame-middle")

    def get_right_text(self) -> str:
        return self._top_child_text("frame-right")

    def get_bottom_text(self) -> str:
        return (
            self.bottom_frame
            .locator("body")
            .inner_text()
            .strip()
        )

    def _top_child_text(self, frame_name: str) -> str:
        """Текст из фрейма, вложенного в frame-top."""
        return (
            self.top_frame
            .frame_locator(f'frame[name="{frame_name}"]')
            .locator("body")
            .inner_text()
            .strip()
        )
