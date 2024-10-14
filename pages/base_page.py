from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        (WebDriverWait(self.driver, 5).until
         (expected_conditions.element_to_be_clickable(locator)))
        self.driver.find_element(*locator).click()

    def return_url(self):
        return self.driver.current_url

    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def find_element_on_page(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def set_element_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_element_text(self, locator):
        return self.find_element_on_page(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def modify_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator
