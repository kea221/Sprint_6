import pytest
import allure
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class Test:
    @allure.title("Проверяем переход на главную страницу при клике на лого 'Самокат'")
    def test_logo_scooter_leads_to_scooter_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.click_on_cookie_button()
        base_page.click_on_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title("Проверяем переход на страницу Дзена при клике на лого 'Яндекс'")
    def test_logo_yandex_leads_to_dzen_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        base_page.click_on_logo_yandex()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        base_page.find_element(BasePageLocators.LOGO_DZEN)
        current_url = driver.current_url
        assert "https://dzen.ru" in current_url
