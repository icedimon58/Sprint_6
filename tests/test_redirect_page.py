import allure
from data import PAGE_URL
from locators.redirect_page_locators import RedirectionPageLocators
from pages.redirect_page import RedirectPage


class TestRedirections:
    @allure.description('Проверка перехода на главную страницу "Самокат"')
    def test_logo_samokat_logo_redirection(self,page_driver):
        Redir = RedirectPage(page_driver)
        Redir.redirect_to(RedirectionPageLocators.ORDER_BUTTON_UP)
        Redir.redirect_to(RedirectionPageLocators.SCOOTER_LOGO)
        with allure.step('Сравнение URL'):
            assert PAGE_URL == Redir.get_redirection_url(RedirectionPageLocators.SCOOTER_LOGO)

    @allure.description('Проверка перехода на страницу "Яндекс.Дзен"')
    def test_logo_yandex_logo_redirection(self,page_driver):
        Redir=RedirectPage(page_driver)
        Redir.redirect_to(RedirectionPageLocators.YANDEX_LOGO)
        with allure.step('Сравнение URL'):
            assert 'dzen.ru' in Redir.get_redirection_url(RedirectionPageLocators.YANDEX_FIND_BTN)