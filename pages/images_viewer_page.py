from pages.base_page import BasePage
from pages.locators import ImagesViewerPageLocators


class ImagesViewerPage(BasePage):
    """Окно для просмотра изображений"""

    def press_next(self):
        """Нажимает кнопку Вперед"""
        self.browser.find_element(*ImagesViewerPageLocators.NEXT_BUTTON).click()

    def press_prev(self):
        """Нажимает кнопку Назад"""
        self.browser.find_element(*ImagesViewerPageLocators.PREV_BUTTON).click()

    def is_image_present(self):
        """Проверяет наличие открытой картинки"""
        return self.is_element_present(*ImagesViewerPageLocators.OPENED_IMAGE)

    def get_current_image_src(self):
        """Возвращает аттрибут src для открытой картинки"""
        return self.browser.find_element(*ImagesViewerPageLocators.OPENED_IMAGE).get_attribute("src")
