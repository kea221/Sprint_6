import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_for_who_locators import OrderForWhoLocators
from locators.about_rent_locators import AboutRentLocators
from constants.constants import Constants
from constants.url_constants import Url

from pages.order_for_who_page import OrderForWho
from pages.about_rent_page import AboutRentPage


class Test:
    @allure.title("Проверяем успешный заказ самоката")
    @pytest.mark.parametrize('date,number_of_days,color,comment', Constants.about_rent)
    def test_scooter_is_ordered(self, driver, date, number_of_days, color, comment):
        order_for_who_page = OrderForWho(driver)
        order_for_who_page.go_to_site(Url.order_url)
        order_for_who_page.click_on_cookie_button()
        order_for_who_page.fill_order_for_who_form(Constants.name, Constants.last_name, Constants.address,
                                                   Constants.station, Constants.number)
        about_rent_page = AboutRentPage(driver)
        about_rent_page.fill_about_rent_form(date, number_of_days, color, comment)
        assert WebDriverWait(driver, 3).until(EC.presence_of_element_located(AboutRentLocators.MODAL_SUCCESS))
