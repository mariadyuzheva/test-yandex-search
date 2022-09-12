from pages.base_page import BasePage
from pages.locators import ImagesSearchResultPageLocators


class ImagesSearchResultPage(BasePage):
    """Страница с результатами поиска по картинкам"""

    def find_search_field(self):
        """Находит на странице поле поиска и возвращает его"""
        return self.browser.find_element(*ImagesSearchResultPageLocators.SEARCH_FIELD)

    def open_first_image(self):
        """Находит ссылку на первую картинку среди результатов поиска по картинкам и переходит по ней"""
        self.browser.find_element(*ImagesSearchResultPageLocators.IMAGE_LINK).click()

    def get_text_in_search_field(self):
        """Возвращает текст из поля поиска"""
        return self.find_search_field().get_attribute("value")
