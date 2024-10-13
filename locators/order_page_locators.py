from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"

    FAMILY_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"

    ADDRESS_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"

    METRO_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"

    STATION_NAME_LOCATOR = By.XPATH, "//*[text()='Бульвар Рокоссовского']"

    PHONE_NBR_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"

    NEXT_BUTTON_LOCATOR = By.XPATH, "//*[text()='Далее']"

    PLACE_DELIVERY_LOCATOR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"

    DATE_LOCATOR = By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]"

    ARENDA_LOCATOR = By.XPATH, "//*[text()='* Срок аренды']"

    DAYS_ARENDA_LOCATOR = By.XPATH, "//*[text()='четверо суток']"

    COLOR_LOCATOR = By.CLASS_NAME, 'Checkbox_Input__14A2w'

    COMMENT_LOCATOR = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'

    ORDER_BUTTON_LOCATOR = By.XPATH, "//div[@class='Order_Buttons__1xGrp']//*[text()='Заказать']"

    YES_BTN_LOCATOR = By.XPATH, "//button[text()='Да']"

    SUCCESSFULL_TXT_LOCATOR=By.CLASS_NAME, "Order_ModalHeader__3FDaJ"
