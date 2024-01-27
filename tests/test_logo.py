import pytest
import allure
from locators.base_page_locators import BasePageLocators
from constants.url_constants import Url
from pages.scooter_page import ScooterPage


class Test:
    @allure.title("Проверяем переход на главную страницу при клике на лого 'Самокат'")
    def test_logo_scooter_leads_to_scooter_page(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site(Url.base_url)
        scooter_page.click_on_cookie_button()
        scooter_page.click_on_logo_scooter()
        assert driver.current_url == Url.base_url

    @allure.title("Проверяем переход на страницу Дзена при клике на лого 'Яндекс'")
    def test_logo_yandex_leads_to_dzen_page(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site(Url.base_url)
        scooter_page.click_on_logo_yandex()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        scooter_page.find_element(BasePageLocators.LOGO_DZEN)
        current_url = driver.current_url
        assert "https://dzen.ru" in current_url
