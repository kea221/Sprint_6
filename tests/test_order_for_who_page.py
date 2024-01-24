import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from locators.order_for_who_locators import OrderForWhoLocators
from constants import Constants
from pages.scooter_page import ScooterPage
from pages.order_for_who_page import OrderForWho


class Test:
    @allure.title("Проверяем переход на страницу заказа по клику на разные кнопки 'Заказать'")
    @pytest.mark.parametrize('button', [BasePageLocators.ORDER_BUTTON_IN_HEADER, BasePageLocators.ORDER_BUTTON])
    def test_go_to_order_for_who(self, driver, button):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        scooter_page.click_on_cookie_button()
        scooter_page.click_on_button_order(button)
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

    @allure.title("Проверяем, что после заполнения формы заказа 'Для кого' переходим на форму 'Про аренду'")
    @pytest.mark.parametrize('name,last_name,address,station,number', Constants.order_form)
    def test_form_order_for_who_is_filled(self, driver, name, last_name, address, station, number):
        order_for_who_page = OrderForWho(driver)
        order_for_who_page.go_to_site('https://qa-scooter.praktikum-services.ru/order')
        order_for_who_page.click_on_cookie_button()
        order_for_who_page.enter_name(name)
        order_for_who_page.enter_last_name(last_name)
        order_for_who_page.enter_address(address)
        order_for_who_page.choose_metro_station(station)
        order_for_who_page.enter_number(number)
        order_for_who_page.click_on_go_button()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderForWhoLocators.RENT_HEADER))
