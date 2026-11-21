from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement

"""
<div class="figure">                              <!-- КАРТОЧКА -->
    <img src="/img/avatar-blank.jpg" ...>          <!-- аватарка -->
    <div class="figcaption">                       <!-- ПОДПИСЬ -->
        <h5>name: user1</h5>                       <!-- имя -->
        <a href="/users/1">View profile</a>        <!-- ссылка -->
    </div>
</div>

в css 
.figcaption { display: none; }                    по умолчанию скрыт 
.figure:hover .figcaption { display: block; }     показывается при наведении на .figure,
                                                    .figcaption внутри .figure, на который наведена мышь 
"""


class HoversPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        """Ведет себя как коллекция карточек"""
        self.all_cards = MultiWebElement(page=page,
                                         locator=self.page.locator(".figure"), # все элементы с этим классом
                                         description="All cards",
                                         )

    def get_count(self) -> int:
        """Возвращает количество карточек figure"""
        return self.all_cards.count()

    def hover_avatar(self, index: int) -> None:
        """Навести мышку на аватарку карточки с номером index."""
        card = self.all_cards.nth(index)  # WebElement для .figure[i]
        # card.locator — это Locator, указывающий на конкретную карточку
        card.locator.locator("img").hover() # затем поиск аватарки внутри карточки и навести мышь

    def get_name(self, index: int) -> str:
        """Прочитать текст <h5> внутри .figcaption карточки index."""
        card = self.all_cards.nth(index)
        return card.locator.locator(".figcaption h5").inner_text() # внутренний + по потомку

    def is_caption_visible(self, index: int) -> bool:
        """Виден ли блок с именем (он виден только при hover)."""
        card = self.all_cards.nth(index)
        return card.locator.locator(".figcaption").is_visible()
