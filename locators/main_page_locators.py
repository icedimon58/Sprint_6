from selenium.webdriver.common.by import By


class MainPageLocators:
    MENU_QUESTION = By.ID, 'accordion__heading-{}'
    MENU_ANSWER = By.ID, 'accordion__panel-{}'
