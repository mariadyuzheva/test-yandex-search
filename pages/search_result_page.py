from pages.base_page import BasePage
from pages.locators import SearchResultPageLocators, BasePageLocators


class SearchResultPage(BasePage):
    """Страница с результатами поиска"""

    def search_result_exists(self):
        """Проверяет наличие таблицы результатов поиска"""
        return self.is_element_present(*SearchResultPageLocators.SEARCH_RESULT)

    def get_first_link(self):
        """Возвращает ссылку на первый результат поиска"""
        search_result = self.browser.find_element(*SearchResultPageLocators.SEARCH_RESULT)
        return search_result.find_element(
            *BasePageLocators.FIRST_LINK).get_attribute("href")
