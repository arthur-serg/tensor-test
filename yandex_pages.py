import time

from base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YaSearchLocators:
    LOCATOR_YA_SEARCH_FIELD = (By.XPATH, "//*[@id=\"text\"]")
    LOCATOR_YA_SEARCH_BUTTON = (By.CLASS_NAME, ".search3__button")
    LOCATOR_YA_SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YA_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YA_LINK = (By.PARTIAL_LINK_TEXT, "tensor.ru")
    LOCATOR_YA_SEARCH_PAGE_TITLE = (By.XPATH, "/html/head/title")
    LOCATOR_YA_MENU_BUTTON = (By.CLASS_NAME, ".services-suggest__icons-more")
    LOCATOR_YA_PICTURES_BUTTON = (By.LINK_TEXT, "https://yandex.ru/images/")


class SearchManager(BasePage):

    def check_search_field(self):
        return self.find_element(YaSearchLocators.LOCATOR_YA_SEARCH_FIELD)

    def check_suggestions(self):
        suggestions_table = self.find_element(YaSearchLocators.LOCATOR_YA_SUGGEST_TABLE, 10)
        return suggestions_table

    def enter_word(self, word):
        search_field = self.check_search_field()
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def press_enter_key(self):
        return self.find_element(YaSearchLocators.LOCATOR_YA_SEARCH_FIELD, time=2).send_keys(Keys.ENTER)

    def check_search_page(self):
        title = self.find_element(YaSearchLocators.LOCATOR_YA_SEARCH_PAGE_TITLE)
        assert "Яндекс: нашлось" in self.driver.title

    def check_search_result(self):
        search_result = self.find_element(YaSearchLocators.LOCATOR_YA_LINK)
        return search_result
