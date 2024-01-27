import pytest
from selenium import webdriver
from locators.scooter_page_locators import ScooterPageLocators
from constants.url_constants import Url


@pytest.fixture
def driver_with_scroll(driver):
    driver.get(Url.base_url)
    element = driver.find_element(*ScooterPageLocators.QUESTION_0)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    yield driver
    driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
