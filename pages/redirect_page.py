import allure
from pages.base_page import BasePage
from locators.redirect_page_locators import RedirectionPageLocators

class RedirectPage(BasePage):

    @allure.step('Переход по элементу')
    def redirect_to(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)
        self.switch_window()

    @allure.step('Поиск кнопки "Заказать"')
    def clic_order_btn(self):
        self.redirect_to(RedirectionPageLocators.ORDER_BUTTON_UP)

    @allure.step('Поиск логотипа "Самокат"')
    def get_samocat_logo(self):
        self.redirect_to(RedirectionPageLocators.SCOOTER_LOGO)

    @allure.step('Поиск логотипа "Яндекс"')
    def get_yandex_logo(self):
        self.redirect_to(RedirectionPageLocators.YANDEX_LOGO)

    @allure.step('Получение URL страницы "Яндекс.Самокат"')
    def get_redirection_url_main(self):
        self.find_element_on_page(RedirectionPageLocators.SCOOTER_LOGO)
        return self.return_url()

    @allure.step('Получение URL страницы')
    def get_redirection_url_yandex(self):
        self.find_element_on_page(RedirectionPageLocators.YANDEX_FIND_BTN)
        return self.return_url()
