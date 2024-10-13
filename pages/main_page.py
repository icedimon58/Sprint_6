import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Поиск вопроса на странице')
    def get_question_to_check(self,locator):
        self.find_element_on_page(locator)
        self.go_to_question(locator)
        self.click_on_question(locator)

    @allure.step('Клик на вопросе')
    def click_on_question(self,locator):
        self.click_on_element(locator)


    @allure.step('Прокрутка страницы')
    def go_to_question(self,locator):
        self.scroll_to_element(locator)


