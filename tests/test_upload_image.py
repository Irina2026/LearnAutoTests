from playwright.sync_api import Page

from pages.upload_image_page import UploadImagePage


def test_upload_file(managed_page: Page, tmp_path):
    # Готовим временный файл, который будем загружать, tmp_path встроенная фикстура, / склеивает пути, удаляется автомат
    file = tmp_path / "test_file.txt"
    file.write_text("hello, world")


    managed_page.goto("/upload")

    page = UploadImagePage(managed_page)


    page.upload_file(str(file))


    assert page.get_heading() == "File Uploaded!"
    assert page.get_file_name() == "test_file.txt"