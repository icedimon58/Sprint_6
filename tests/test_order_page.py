import allure
import pytest

from data import TEST_DATA_1,TEST_DATA_2
from pages.order_page import OrderPage
from locators.redirect_page_locators import RedirectionPageLocators as RPL


class TestOrderPage:
    @allure.description('Проверка оформления заказа через кнопку')
    @pytest.mark.parametrize('locator,name,fam,sity,phone,comment', [
        (RPL.ORDER_BUTTON_BIG,*TEST_DATA_1),
        (RPL.ORDER_BUTTON_BIG, *TEST_DATA_2),
        (RPL.ORDER_BUTTON_UP,*TEST_DATA_2)])
    def test_order_page_btn_bottom(self, page_driver, locator,name,fam,sity,phone,comment):
        OrderPageTest = OrderPage(page_driver)
        OrderPageTest.redir_to_order_page(locator)
        OrderPageTest.set_name(name)
        OrderPageTest.set_family(fam)
        OrderPageTest.set_addres(sity)
        OrderPageTest.set_metro_station()
        OrderPageTest.set_phone(phone)
        OrderPageTest.click_next_btn()
        OrderPageTest.set_place_to_delivery()
        OrderPageTest.set_date_to_delivery()
        OrderPageTest.set_arenda_days()
        OrderPageTest.set_color()
        OrderPageTest.set_comment(comment)
        with allure.step('Проверка подтверждения заказа'):
            assert 'Заказ оформлен' in OrderPageTest.confirm_order()
