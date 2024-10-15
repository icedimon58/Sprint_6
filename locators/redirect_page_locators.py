from selenium.webdriver.common.by import By


class RedirectionPageLocators:

    SCOOTER_LOGO = By.XPATH,"//img[@alt='Scooter']"

    YANDEX_FIND_BTN = By.XPATH,"//button[text()='Найти']"

    YANDEX_LOGO = By.XPATH, "//img[@alt='Yandex']"

    ORDER_BUTTON_BIG = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button"

    ORDER_BUTTON_UP = By.CLASS_NAME, "Button_Button__ra12g"