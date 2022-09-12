from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """Главная страница"""

    def __init__(self, browser):
        super().__init__(browser, "https://www.yandex.ru/")

    def is_search_field_present(self):
        """Проверяет наличие поля поиска"""
        return self.is_element_present(*MainPageLocators.SEARCH_FIELD)

    def enter_search_text(self, text):
        """Вводит текст в поле поиска"""
        self.browser.find_element(*MainPageLocators.SEARCH_FIELD).send_keys(text)

    def is_search_suggest_present(self):
        """Проверяет наличие таблицы с подсказками (suggest)"""
        return self.is_element_present(*MainPageLocators.SEARCH_SUGGEST)

    def is_images_link_present(self):
        """Проверяет наличие ссылки 'Картинки'"""
        return self.is_element_present(*MainPageLocators.IMAGES_LINK)

    def click_images_link(self):
        """Переходит по ссылке 'Картинки'"""
        self.browser.find_element(*MainPageLocators.IMAGES_LINK).click()
