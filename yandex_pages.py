from base import BasePage
from selenium.webdriver.common.by import By


class YaSearchLocators:
    LOCATOR_YA_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YA_SEARCH_BUTTON = (By.CLASS_NAME, "search3__button")  # mini-suggest__button
    LOCATOR_YA_SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YA_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YA_LINK = (By.PARTIAL_LINK_TEXT, "tensor.ru")
    LOCATOR_YA_SEARCH_RESULT = (By.XPATH, "/html/head/title")
    LOCATOR_YA_MENU_BUTTON = (By.CLASS_NAME, "services-suggest__icons-more")
    LOCATOR_YA_PICTURES_BUTTON = (By.LINK_TEXT, "https://yandex.ru/images/")


class SearchManager(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YaSearchLocators.LOCATOR_YA_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def check_suggestions(self):
        suggestions_table = self.find_element(YaSearchLocators.LOCATOR_YA_SUGGEST_TABLE)
        return suggestions_table

    def click_on_the_search_button(self):
        return self.find_element(YaSearchLocators.LOCATOR_YA_SEARCH_BUTTON, time=2).click()

    def check_search_result(self):
        return self.find_element(YaSearchLocators.LOCATOR_YA_SEARCH_RESULT)
