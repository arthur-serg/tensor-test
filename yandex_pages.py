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
    SELECTED_IMAGE = (By.CSS_SELECTOR, "div[class=MMThumbImage-Image]")


class SearchManager(BasePage):

    def check_search_field(self):
        search_field = self.find_element(YandexLocators.SEARCH_FIELD)
        assert search_field is not None
        self.my_logger.debug(f"search field {search_field} was found")
        return search_field

    def check_suggestions(self):
        suggestions_table = self.find_element(YandexLocators.SUGGEST_TABLE, 10)
        assert suggestions_table is not None
        self.my_logger.debug(f"suggestions table {suggestions_table} was found")
        return suggestions_table

    def enter_word(self, word):
        search_field = self.check_search_field()
        self.my_logger.debug(f"search field {search_field} was found")
        search_field.click()
        self.my_logger.debug(f"search field {search_field} was clicked")
        search_field.send_keys(word)
        self.my_logger.debug(f"word {word} was sent")
        return search_field

    def press_enter_key(self):
        return self.find_element(YandexLocators.SEARCH_FIELD, time=2).send_keys(Keys.ENTER)

    def check_search_page(self):
        title = self.find_element(YandexLocators.SEARCH_PAGE_TITLE)
        self.my_logger.debug(f"title {title} of the page was found")
        assert "Яндекс: нашлось" in self.driver.title

    def check_search_result(self):
        search_result = self.find_element(YandexLocators.TARGET_LINK)
        self.my_logger.debug(f"search result {search_result} on page was found")
        assert search_result is not None
        return search_result


class ImageSearchManager(BasePage):

    def check_menu_button(self):
        # time.sleep(20) #DEBUG CAPTCHA

        search_field = self.find_element(YandexLocators.SEARCH_FIELD)
        self.my_logger.debug(f"search field {search_field} was found")
        search_field.click()
        self.my_logger.debug(f"search field {search_field} was clicked")
        menu_button = self.find_element(YandexLocators.MENU_BUTTON)
        self.my_logger.debug(f"menu button {menu_button} was found")
        assert menu_button is not None
        return

    def open_menu_click_images(self):
        menu_button = self.find_element(YandexLocators.MENU_BUTTON)
        self.my_logger.debug(f"menu button {menu_button} was found")
        menu_button.click()
        self.my_logger.debug(f"menu button {menu_button} was clicked")
        images_button = self.find_element(YandexLocators.IMAGES_BUTTON)
        self.my_logger.debug(f"images button {images_button} was found")
        images_button.click()
        self.my_logger.debug(f"images button {images_button} was clicked")
        assert images_button is not None

    def check_images_url(self):
        browser_windows = self.driver.window_handles
        self.driver.switch_to.window(browser_windows[-1])
        self.my_logger.debug(f"browser window switched to {browser_windows[-1]}")
        self.my_logger.debug(f"current url changed to {self.driver.current_url}")
        assert self.driver.current_url == "https://yandex.ru/images/"

    def open_first_category(self):
        target_images = self.find_element(YandexLocators.IMAGES_FIRST_CATEGORY)
        self.my_logger.debug(f"images {target_images} was found")
        target_images.click()
        self.my_logger.debug(f"images {target_images} was clicked")
        assert target_images is not None

    def check_search_field_text(self):
        target_images = self.find_element(YandexLocators.IMAGES_FIRST_CATEGORY)
        self.my_logger.debug(f"images {target_images} was found")
        search_field = self.find_element(YandexLocators.SEARCH_INPUT)
        self.my_logger.debug(f"search field {search_field} was found")
        category_title = target_images.get_attribute('innerText')
        self.my_logger.debug(f"search field text is: {category_title}")
        assert search_field.get_attribute('value') == category_title

    def open_and_check_image(self):
        root_image = self.find_element(YandexLocators.ROOT_IMAGE)
        self.my_logger.debug(f"first image {root_image} was found")
        root_image.click()
        self.my_logger.debug(f"first image {root_image} was clicked")
        media_viewer = self.find_element(YandexLocators.MEDIA_VIEWER)
        self.my_logger.debug(f"yandex media viewer {media_viewer} was found")
        assert media_viewer is not None

    def go_forward_check_image_and_go_backward(self):
        gallery_container = self.find_element((By.CSS_SELECTOR, ".MMGallery-Container"))
        self.my_logger.debug(f"gallery container {gallery_container} was found")
        all_childs = self.driver.find_element(By.CSS_SELECTOR, ".MMGallery-Container").find_elements(
            By.CSS_SELECTOR, "*")
        self.my_logger.debug(f"there is {len(all_childs)} childs of gallery container")
        first_image_index = 0
        next_image_index = 0

        for i in range(len(all_childs)):
            selected_item = self.driver.find_element(By.CSS_SELECTOR, ".MMGallery-Item.MMGallery-Item_selected")
            if (all_childs[i] == selected_item):
                first_image_index = i

        assert gallery_container is not None, "gallery container was not found"

        first_image = self.find_element(YandexLocators.SELECTED_IMAGE)
        self.my_logger.debug(f"first image {first_image} was found")
        assert first_image is not None
        assert first_image_index is not None

        forward_button = self.find_element(YandexLocators.FWD_BUTTON)
        self.my_logger.debug(f"forward button {forward_button} was found")
        assert forward_button is not None

        forward_button.click()
        self.my_logger.debug(f"forward button {forward_button} was clicked")
        next_image = self.find_element(YandexLocators.SELECTED_IMAGE)
        self.my_logger.debug(f"next image {next_image} was found")
        for i in range(len(all_childs)):
            selected_item = self.driver.find_element(By.CSS_SELECTOR, ".MMGallery-Item.MMGallery-Item_selected")
            if (all_childs[i] == selected_item):
                next_image_index = i

        assert next_image is not None
        assert next_image_index != first_image_index, "Image was not changed after forward navigation"

        backward_button = self.find_element(YandexLocators.BACK_BUTTON)
        self.my_logger.debug(f"backward button {backward_button} was found")
        assert backward_button is not None

        backward_button.click()
        self.my_logger.debug(f"backward button {backward_button} was clicked")
        next_image = self.find_element(YandexLocators.SELECTED_IMAGE)

        assert next_image is not None
        self.my_logger.debug(f"image {next_image} after backwards was found")
        for i in range(len(all_childs)):
            selected_item = self.driver.find_element(By.CSS_SELECTOR, ".MMGallery-Item.MMGallery-Item_selected")
            if (all_childs[i] == selected_item):
                next_image_index = i

        assert next_image_index == first_image_index, "Image was not changed after backward navigation"
