import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from locators.order_for_who_locators import OrderForWhoLocators
from locators.about_rent_locators import AboutRentLocators
from constants import Constants

from pages.order_for_who_page import OrderForWho
from pages.about_rent_page import AboutRentPage


class Test:
    @allure.title("Проверяем успешный заказ самоката")
    @pytest.mark.parametrize('date,number_of_days,color,comment', Constants.about_rent)
    def test_scooter_is_ordered(self, driver, date, number_of_days, color, comment):
        order_for_who_page = OrderForWho(driver)
        order_for_who_page.go_to_site('https://qa-scooter.praktikum-services.ru/order')
        order_for_who_page.click_on_cookie_button()
        order_for_who_page.enter_name("Иван")
        order_for_who_page.enter_last_name("Сусанин")
        order_for_who_page.enter_address("ул.Лесная, д.15")
        order_for_who_page.choose_metro_station(OrderForWhoLocators.STATION_1)
        order_for_who_page.enter_number("89994561212")
        order_for_who_page.click_on_go_button()
        about_rent_page = AboutRentPage(driver)
        about_rent_page.choose_date(date)
        about_rent_page.choose_rental_period(number_of_days)
        about_rent_page.choose_color(color)
        about_rent_page.enter_comment(comment)
        about_rent_page.click_order()
        about_rent_page.click_yes()
        assert WebDriverWait(driver, 3).until(EC.presence_of_element_located(AboutRentLocators.MODAL_SUCCESS))
