from selenium.webdriver import Keys

from pages.images_page import ImagesPage
from pages.images_search_result_page import ImagesSearchResultPage
from pages.images_viewer_page import ImagesViewerPage
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage


def test_text_search(browser):
    """
    Проверяет наличие поля поиска, таблицы с подсказками и
    результатов поиска на yandex.ru
    """
    main_page = MainPage(browser)
    # 1. Зайти на yandex.ru
    main_page.open()
    # 2. Проверить наличие поля поиска
    assert main_page.is_search_field_present(), "Отсутствует поле поиска"

    # 3. Ввести в поиск "Тензор"
    main_page.enter_search_text("Тензор")
    # 4. Проверить, что появилась таблица с подсказками
    assert main_page.is_search_suggest_present(), \
        "Отсутствует таблица с подсказками (suggest)"

    # 5. При нажатии Enter появляется таблица результатов поиска
    main_page.enter_search_text(Keys.ENTER)
    yandex_search_result_page = SearchResultPage(browser, browser.current_url)
    assert yandex_search_result_page.search_result_exists(), \
        "Отсутствует таблица результатов поиска"

    # 6. Проверить, что первая ссылка ведет на сайт tensor.ru
    first_link = yandex_search_result_page.get_first_link()
    assert first_link == "https://tensor.ru/" or \
        first_link == "http://tensor.ru/", \
        "Первая ссылка не ведет на сайт tensor.ru"


def test_images_search(browser):
    """Проверяет работу поиска по картинкам на yandex.ru"""
    main_page = MainPage(browser)
    # 1. Зайти на yandex.ru
    main_page.open()
    # 2. Проверить, что ссылка «Картинки» присутствует на странице
    assert main_page.is_images_link_present(), \
        "Ссылка 'Картинки' отсутствует на странице"
    # 3. Кликаем на ссылку
    main_page.click_images_link()
    browser.switch_to.window(browser.window_handles[-1])

    # 4. Проверить, что перешли на url https://yandex.ru/images/
    assert browser.current_url.startswith("https://yandex.ru/images/"), \
        "Переход на неверный url"
    images_page = ImagesPage(browser, browser.current_url)
    # 5. Открыть первую категорию
    first_category_name = images_page.open_first_category_and_get_name()
    images_search_result_page = ImagesSearchResultPage(
        browser, browser.current_url)

    # 6. Проверить, что название категории отображается в поле поиска
    assert images_search_result_page.get_text_in_search_field() == \
        first_category_name,\
        "Название категории не отображается в поле поиска"

    # 7. Открыть первую картинку
    images_search_result_page.open_first_image()
    images_viewer_page = ImagesViewerPage(browser, browser.current_url)

    # 8. Проверить, что картинка открылась
    assert images_viewer_page.is_image_present(), "Картинка не открылась"
    first_image_src = images_viewer_page.get_current_image_src()

    # 9. Нажать кнопку вперед
    images_viewer_page.press_next()
    # 10. Проверить, что картинка сменилась
    assert images_viewer_page.get_current_image_src() != first_image_src, \
        "Картинка не сменилась"
    # 11. Нажать назад
    images_viewer_page.press_prev()
    # 12. Проверить, что картинка осталась из шага 8
    assert images_viewer_page.get_current_image_src() == first_image_src, \
        "Картинка не меняется на предыдущую при нажатии кнопки 'Назад'"
