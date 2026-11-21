from pathlib import Path
from playwright.sync_api import Page
from pages.file_download_page import FileDownloadPage


def test_download_third_file(managed_page: Page, tmp_path: Path):
    managed_page.goto("/download")
    page = FileDownloadPage(managed_page)

    expected_name = page.get_file_name_by_index(3)
    assert expected_name == "Images.txt"
    """
    Шаг 3 — download_file_by_index(3):
    входит в expect_download();
    кликает третью ссылку;
    Playwright дожидается начала скачивания и возвращает Download
    """
    download = page.download_file_by_index(3)
    #download.suggested_filename — имя, которое сервер прислал при скачивании
    assert download.suggested_filename == expected_name