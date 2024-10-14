import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators as MPL
from data import ANSWER


class TestMainPage:
    @allure.description('Проверка ответа на вопрос')
    @pytest.mark.parametrize('num,locator_q,locator_a',
                             [[0, MPL.MENU_QUESTION, MPL.MENU_ANSWER],
                              [1, MPL.MENU_QUESTION, MPL.MENU_ANSWER],
                              [2, MPL.MENU_QUESTION, MPL.MENU_ANSWER],
                              [3, MPL.MENU_QUESTION, MPL.MENU_ANSWER],
                              [4, MPL.MENU_QUESTION, MPL.MENU_ANSWER],
                              [5, MPL.MENU_QUESTION, MPL.MENU_ANSWER],
                              [6, MPL.MENU_QUESTION, MPL.MENU_ANSWER],
                              [7, MPL.MENU_QUESTION, MPL.MENU_ANSWER]]
                             )
    def test_questions(self, page_driver, num, locator_q, locator_a):
        main_page_test = MainPage(page_driver)
        element1 = main_page_test.modify_locators(locator_q, num)
        main_page_test.get_question_to_check(element1)
        element2 = main_page_test.modify_locators(locator_a, num)
        with allure.step("Сравниваем текст ответа с эталоном"):
            assert main_page_test.get_element_text(element2) == ANSWER[num]
