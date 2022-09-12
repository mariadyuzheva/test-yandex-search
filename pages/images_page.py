from pages.base_page import BasePage
from pages.locators import ImagesPageLocators, BasePageLocators


class ImagesPage(BasePage):
    """Страница с категориями поиска по картинкам"""

    def open_first_category_and_get_name(self):
        """Открывает первую категорию изображений и возвращает название этой категории"""
        first_category = self.browser.find_element(
            *ImagesPageLocators.CATEGORIES).find_element(
            *BasePageLocators.FIRST_LINK)
        first_category.click()
        return first_category.text
