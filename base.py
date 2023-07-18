from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import os
from datetime import datetime


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"
        self.log_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f.log')
        self.my_logger = logger
        if (os.path.isdir("logs")):
            os.chdir("logs")
            self.my_logger.add(self.log_filename, format="{time} {level} {message}", backtrace=True)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
