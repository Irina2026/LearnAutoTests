from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class DynamicImagesPage(BasePage):
    MAX_REFRESHES = 30 #бесконечный цикл долго, лучше несколько раз по 30,
    # также, если на странице баг, не выйдем никогда, обсуждаемо

    def __init__(self, page: Page):
        super().__init__(page)
        # .example img — 3 нужных картинки, если просто img, то цепляет лого гитхаба сверху
        self.avatars = MultiWebElement(
            page=page,
            locator=page.locator(".example img"),
            description="Avatars",
        )

    def get_srcs(self) -> list[str]:
        """Возвращает список всех аватарок"""
        return [img.get_attribute("src") for img in self.avatars]

    def find_duplicate(self) -> str | None:
        """Вернуть src, который встречается хотя бы дважды, либо None."""
        seen = set()
        for src in self.get_srcs():
            if src in seen:
                return src
            seen.add(src)
        return None

    def refresh_until_duplicate(self) -> str:
        """Обновлять страницу, пока не найдётся пара одинаковых картинок."""
        for _ in range(self.MAX_REFRESHES):
            dup = self.find_duplicate() # поискать на текущей странице сразу,
                                        # в условии задаче не указан минимум обновлений
            if dup:
                return dup
            self.page_actions.reload()

        raise AssertionError(
            f"Нет пары за {self.MAX_REFRESHES} обновлений. srcs: {self.get_srcs()}"
        )