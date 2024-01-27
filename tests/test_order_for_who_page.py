import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators
from locators.order_for_who_locators import OrderForWhoLocators
from constants.constants import Constants
from constants.url_constants import Url

from pages.scooter_page import ScooterPage
from pages.order_for_who_page import OrderForWho


class Test:
    @allure.title("Проверяем переход на страницу заказа по клику на разные кнопки 'Заказать'")
    @pytest.mark.parametrize('button', [BasePageLocators.ORDER_BUTTON_IN_HEADER, BasePageLocators.ORDER_BUTTON])
    def test_go_to_order_for_who(self, driver, button):
        scooter_page = ScooterPage(driver)
        scooter_page.go_to_site(Url.base_url)
        scooter_page.click_on_cookie_button()
        scooter_page.click_on_button_order(button)
        assert driver.current_url == Url.order_url

    @allure.title("Проверяем, что после заполнения формы заказа 'Для кого' переходим на форму 'Про аренду'")
    @pytest.mark.parametrize('name,last_name,address,station,number', Constants.order_form)
    def test_form_order_for_who_is_filled(self, driver, name, last_name, address, station, number):
        order_for_who_page = OrderForWho(driver)
        order_for_who_page.go_to_site(Url.order_url)
        order_for_who_page.click_on_cookie_button()
        order_for_who_page.fill_order_for_who_form(name, last_name, address, station, number)
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderForWhoLocators.RENT_HEADER))
