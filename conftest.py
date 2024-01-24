import pytest
from selenium import webdriver
from locators.scooter_page_locators import ScooterPageLocators


@pytest.fixture
def driver_with_scroll(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    element = driver.find_element(*ScooterPageLocators.QUESTION_0)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    yield driver
    driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
