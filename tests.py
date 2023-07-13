from yandex_pages import SearchManager


def test_ya_search(browser):
    ya_main_page = SearchManager(browser)
    ya_main_page.go_to_site()
    ya_main_page.enter_word("Тензор")
    ya_main_page.check_suggestions()
    ya_main_page.click_on_the_search_button()
    ya_main_page.check_search_result()
