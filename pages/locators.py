from selenium.webdriver.common.by import By


class BasePageLocators:
    FIRST_LINK = (By.TAG_NAME, "a")


class MainPageLocators:
    SEARCH_FIELD = (By.ID, "text")
    SEARCH_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup")
    IMAGES_LINK = (By.LINK_TEXT, "Картинки")


class SearchResultPageLocators:
    SEARCH_RESULT = (By.ID, "search-result")


class ImagesPageLocators:
    CATEGORIES = (By.CLASS_NAME, "PopularRequestList")


class ImagesSearchResultPageLocators:
    SEARCH_FIELD = (By.NAME, "text")
    IMAGE_LINK = (By.CLASS_NAME, "serp-item__link")


class ImagesViewerPageLocators:
    NEXT_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    PREV_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")
    OPENED_IMAGE = (By.CLASS_NAME, "MMImage-Origin")
