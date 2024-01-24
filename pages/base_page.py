import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step("Кликнуть на кнопку принятия куки")
    def click_on_cookie_button(self, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(BasePageLocators.COOKIE_BUTTON)).click()

    @allure.step("Дождаться появления элемента")
    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть на логотип 'Самокат' в шапке")
    def click_on_logo_scooter(self, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(BasePageLocators.LOGO_SAMOKAT)).click()

    @allure.step("Кликнуть на логотип 'Яндекс' в шапке")
    def click_on_logo_yandex(self, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(BasePageLocators.LOGO_YANDEX)).click()
