from yandex_pages import SearchManager
from yandex_pages import ImageSearchManager


def test_ya_search(browser):
    ya_main_page = SearchManager(browser)
    ya_main_page.go_to_site()
    ya_main_page.check_search_field()
    ya_main_page.enter_word("Тензор")
    ya_main_page.check_suggestions()
    ya_main_page.press_enter_key()
    ya_main_page.check_search_page()
    ya_main_page.check_search_result()


def test_yandex_images(browser):
    image_search = ImageSearchManager(browser)
    image_search.go_to_site()
    image_search.check_menu_button()
    image_search.open_menu_click_images()
    image_search.check_images_url()
    image_search.open_first_category()
    image_search.check_search_field_text()
    image_search.open_and_check_image()
    image_search.navigate_forward()
    image_search.check_is_image_changed()
    image_search.navigate_backwards()
    image_search.check_image()
