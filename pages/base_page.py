from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открывает страницу в браузере"""
        self.browser.get(self.url)

    def is_element_present(self, locator, value):
        """Проверяет наличие элемента на странице по локатору"""
        try:
            self.browser.find_element(locator, value)
        except NoSuchElementException:
            return False
        return True

    def switch_to_last_opened_window(self):
        """Переключается на последнее открытое окно"""
        self.browser.switch_to.window(self.browser.window_handles[-1])
        # Для браузера Firefox, иначе current_url имеет значение about:blank
        WebDriverWait(self.browser, 10).until(EC.url_changes("about:blank"))
