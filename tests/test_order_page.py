import allure
import pytest

from data import TEST_DATA_1, TEST_DATA_2, PAGE_URL
from pages.order_page import OrderPage
from locators.redirect_page_locators import RedirectionPageLocators as RPL


class TestOrderPage:
    @allure.description('Проверка оформления заказа через кнопку')
    @allure.title('Тест страницы заказа с параметрами')
    @allure.link(PAGE_URL, name='Тестовая страница "Яндекс.Самокат"')
    @pytest.mark.parametrize('locator,name,fam,sity,phone,comment', [
        (RPL.ORDER_BUTTON_BIG,*TEST_DATA_1),
        (RPL.ORDER_BUTTON_BIG, *TEST_DATA_2),
        (RPL.ORDER_BUTTON_UP,*TEST_DATA_2)])
    def test_order_page_btn_bottom(self, page_driver, locator,name,fam,sity,phone,comment):
        order_page_test = OrderPage(page_driver)
        order_page_test.redir_to_order_page(locator)
        order_page_test.set_name(name)
        order_page_test.set_family(fam)
        order_page_test.set_addres(sity)
        order_page_test.set_metro_station()
        order_page_test.set_phone(phone)
        order_page_test.click_next_btn()
        order_page_test.set_place_to_delivery()
        order_page_test.set_date_to_delivery()
        order_page_test.set_arenda_days()
        order_page_test.set_color()
        order_page_test.set_comment(comment)
        with allure.step('Проверка подтверждения заказа'):
            assert 'Заказ оформлен' in order_page_test.confirm_order()
