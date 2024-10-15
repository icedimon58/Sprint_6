import pytest
from selenium import webdriver
from data import PAGE_URL


@pytest.fixture()
def page_driver():
    driver = webdriver.Firefox()
    driver.get(PAGE_URL)
    yield driver
    driver.quit()
