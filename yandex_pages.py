import time

from base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class YandexLocators:
    SEARCH_FIELD = (By.XPATH, "//*[@id=\"text\"]")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search2__input .input__control")
    SEARCH_BUTTON = (By.CLASS_NAME, ".search3__button")
    SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__popup-content")
    NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    TARGET_LINK = (By.PARTIAL_LINK_TEXT, "tensor.ru")
    SEARCH_PAGE_TITLE = (By.XPATH, "/html/head/title")
    MENU_BUTTON = (By.CLASS_NAME, "services-suggest__item-more")
    IMAGES_BUTTON = (By.CSS_SELECTOR, ".services-more-popup__section-all a[aria-label='Картинки']")
    IMAGES_LINK = (By.PARTIAL_LINK_TEXT, "yandex.ru/images")
    IMAGES_FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item.PopularRequestList-Item_pos_0")
    SEARCH_TEXT = (
        By.CLASS_NAME, ".PopularRequestList-Item.PopularRequestList-Item_pos_0 .PopularRequestList-SearchText")
    ROOT_IMAGE = (By.CSS_SELECTOR, ".serp-item_pos_0 .serp-item__link")
    MEDIA_VIEWER = (By.CSS_SELECTOR, ".MMViewerModal .Modal-Content[class]")
    FWD_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next .CircleButton-Icon")
    BACK_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev .CircleButton-Icon")


class SearchManager(BasePage):

    def check_search_field(self):
        assert self.find_element(YandexLocators.SEARCH_FIELD) is not None
        return self.find_element(YandexLocators.SEARCH_FIELD)

    def check_suggestions(self):
        suggestions_table = self.find_element(YandexLocators.SUGGEST_TABLE, 10)
        assert suggestions_table is not None
        return suggestions_table

    def enter_word(self, word):
        search_field = self.check_search_field()
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def press_enter_key(self):
        return self.find_element(YandexLocators.SEARCH_FIELD, time=2).send_keys(Keys.ENTER)

    def check_search_page(self):
        title = self.find_element(YandexLocators.SEARCH_PAGE_TITLE)
        assert "Яндекс: нашлось" in self.driver.title

    def check_search_result(self):
        search_result = self.find_element(YandexLocators.TARGET_LINK)
        assert search_result is not None
        return search_result


class ImageSearchManager(BasePage):

    def check_menu_button(self):
        search_field = self.find_element(YandexLocators.SEARCH_FIELD)
        search_field.click()
        menu_button = self.find_element(YandexLocators.MENU_BUTTON)
        assert menu_button is not None

    def open_menu_click_images(self):
        menu_button = self.find_element(YandexLocators.MENU_BUTTON)
        menu_button.click()
        images_button = self.find_element(YandexLocators.IMAGES_BUTTON)
        images_button.click()
        assert images_button is not None

    def check_images_url(self):
        browser_windows = self.driver.window_handles
        self.driver.switch_to.window(browser_windows[-1])
        assert self.driver.current_url == "https://yandex.ru/images/"

    def open_first_category(self):
        target_images = self.find_element(YandexLocators.IMAGES_FIRST_CATEGORY)
        target_images.click()
        assert target_images is not None

    def check_search_field_text(self):
        target_images = self.find_element(YandexLocators.IMAGES_FIRST_CATEGORY)
        search_field = self.find_element(YandexLocators.SEARCH_INPUT)
        category_title = target_images.get_attribute('innerText')
        assert search_field.get_attribute('value') == category_title

    def open_and_check_image(self):
        time.sleep(15)  # DEBUG CAPTCHA
        root_image = self.find_element(YandexLocators.ROOT_IMAGE)
        root_image.click()
        media_viewer = self.find_element(YandexLocators.MEDIA_VIEWER)
        assert media_viewer is not None

    def navigate_forward(self):
        pass

    def check_is_image_changed(self):
        pass

    def navigate_backwards(self):
        pass

    def check_image(self):
        pass
