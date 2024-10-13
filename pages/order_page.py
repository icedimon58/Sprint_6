import allure
from locators.order_page_locators import OrderPageLocators as OPL
from pages.base_page import BasePage
from pages.redirect_page import RedirectPage


class OrderPage(RedirectPage,BasePage):

    def redir_to_order_page(self,locator):
        self.redirect_to(locator)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.set_element_text(OPL.NAME_LOCATOR,name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_family(self,family):
        self.set_element_text(OPL.FAMILY_LOCATOR, family)

    @allure.step('Заполнение поля "Адрес"')
    def set_addres(self,sity):
        self.set_element_text(OPL.ADDRESS_LOCATOR, sity)

    @allure.step('Выбор станции метро')
    def set_metro_station(self):
        self.click_on_element(OPL.METRO_LOCATOR)
        self.click_on_element(OPL.STATION_NAME_LOCATOR)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self,phone):
        self.set_element_text(OPL.PHONE_NBR_LOCATOR,phone)

    def click_next_btn(self):
        self.click_on_element(OPL.NEXT_BUTTON_LOCATOR)

    @allure.step('Выбор даты доставки')
    def set_place_to_delivery(self):
        self.click_on_element(OPL.PLACE_DELIVERY_LOCATOR)

    def set_date_to_delivery(self):
        self.click_on_element(OPL.DATE_LOCATOR)

    @allure.step('Выбор срока аренды')
    def set_arenda_days(self):
        self.click_on_element(OPL.ARENDA_LOCATOR)
        self.click_on_element(OPL.DAYS_ARENDA_LOCATOR)

    @allure.step('Выбор цвета')
    def set_color(self):
        self.click_on_element(OPL.COLOR_LOCATOR)

    @allure.step('Заполнение поля "Комментарий"')
    def set_comment(self,comment):
        self.set_element_text(OPL.COMMENT_LOCATOR,comment)


    def confirm_order(self):
        self.click_on_element(OPL.ORDER_BUTTON_LOCATOR)
        self.click_on_element(OPL.YES_BTN_LOCATOR)
        return self.get_element_text(OPL.SUCCESSFULL_TXT_LOCATOR)



