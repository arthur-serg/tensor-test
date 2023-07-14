from yandex_pages import SearchManager


def test_ya_search(browser):
    ya_main_page = SearchManager(browser)
    ya_main_page.go_to_site()
    ya_main_page.check_search_field()
    ya_main_page.enter_word("Тензор")
    ya_main_page.check_suggestions()
    ya_main_page.press_enter_key()
    ya_main_page.check_search_page()
    ya_main_page.check_search_result()
