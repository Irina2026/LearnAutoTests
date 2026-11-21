from playwright.sync_api import Page, Download

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class FileDownloadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.file_links = MultiWebElement(
            page=page,
            locator=page.locator(".example a"),
            description="File links",
        )

    def get_file_name_by_index(self, index: int) -> str:
        return self.file_links.nth(index - 1).get_inner_text().strip()

    def download_file_by_index(self, index: int) -> Download:
        """
        page.expect_download() — обязательный контекст-менеджер в Playwright. Без него клик по ссылке запустит
        скачивание, но Playwright не «поймает» объект Download, и файл останется только во временной папке браузера
        без доступа к имени/пути.
        download_info.value — объект Download с методами:
        .suggested_filename — имя, которое сервер предложил (из Content-Disposition или последнего сегмента URL);
        .save_as(path) — сохранить по пути;
        .path() — временный путь скачанного файла.
        """
        with self.page.expect_download() as download_info:
            self.file_links.nth(index - 1).click()
        return download_info.value