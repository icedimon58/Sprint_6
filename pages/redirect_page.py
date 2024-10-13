import allure
from pages.base_page import BasePage


class RedirectPage(BasePage):

    @allure.step('Переход по элементу')
    def redirect_to(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def get_redirection_url(self, locator):
        self.find_element_on_page(locator)
        return self.driver.current_url
