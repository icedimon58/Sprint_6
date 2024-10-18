import allure
from data import PAGE_URL
from pages.redirect_page import RedirectPage


class TestRedirections:
    @allure.title('Тест перехода на главную страницу "Самокат"')
    @allure.link(PAGE_URL,name='Тестовая страница "Яндекс.Самокат"')
    @allure.description('Проверка перехода на главную страницу "Самокат"')
    def test_logo_samokat_logo_redirection(self,page_driver):
        redir_page = RedirectPage(page_driver)
        redir_page.clic_order_btn()
        redir_page.get_samocat_logo()
        with allure.step('Сравнение URL'):
            assert PAGE_URL == redir_page.get_redirection_url_main()

    @allure.title('Тест перехода на страницу "Яндекс.Дзен"')
    @allure.description('Проверка перехода на страницу "Яндекс.Дзен"')
    @allure.link(PAGE_URL, name='Тестовая страница "Яндекс.Самокат"')
    def test_logo_yandex_logo_redirection(self,page_driver):
        redir_page = RedirectPage(page_driver)
        redir_page.get_yandex_logo()
        with allure.step('Сравнение URL'):
            assert 'dzen.ru' in redir_page.get_redirection_url_yandex()