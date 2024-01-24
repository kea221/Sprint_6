import allure
import pytest
from pages.base_page import BasePage
from locators.order_for_who_locators import OrderForWhoLocators


class OrderForWho(BasePage):
    @allure.step("Ввести имя в поле ввода имени")
    def enter_name(self, name):
        return self.find_element(OrderForWhoLocators.NAME_FIELD).send_keys(name)

    @allure.step("Ввести фамилию в поле ввода фамилии")
    def enter_last_name(self, last_name):
        return self.find_element(OrderForWhoLocators.LAST_NAME_FIELD).send_keys(last_name)

    @allure.step("Ввести адрес в поле ввода адреса")
    def enter_address(self, address):
        return self.find_element(OrderForWhoLocators.ADDRESS_FIELD).send_keys(address)

    @allure.step("Выбрать станцию метро из выпадающего списка")
    def choose_metro_station(self, station):
        self.find_element(OrderForWhoLocators.METRO).click()
        return self.find_element(station).click()

    @allure.step("Ввести номер телефона")
    def enter_number(self, number):
        return self.find_element(OrderForWhoLocators.NUMBER_FIELD).send_keys(number)

    @allure.step("Кликнуть на кнопку 'Далее'")
    def click_on_go_button(self):
        return self.find_element(OrderForWhoLocators.BUTTON_GO).click()
