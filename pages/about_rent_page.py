import pytest
import allure
from pages.base_page import BasePage
from locators.about_rent_locators import AboutRentLocators


class AboutRentPage(BasePage):
    @allure.step("Выбрать дату в календаре")
    def choose_date(self, date):
        self.find_element(AboutRentLocators.DATE_FIELD).click()
        self.find_element(AboutRentLocators.CALENDAR)
        return self.find_element(date).click()

    @allure.step("Выбрать срок аренды из выпадающего списка")
    def choose_rental_period(self, number_of_days):
        self.find_element(AboutRentLocators.RENTAL_PERIOD_FIELD).click()
        self.find_element(AboutRentLocators.RENTAL_PERIOD_MENU)
        return self.find_element(number_of_days).click()

    @allure.step("Выбрать цвет самоката")
    def choose_color(self, color):
        return self.find_element(color).click()

    @allure.step("Оставить комментарий")
    def enter_comment(self, comment):
        return self.find_element(AboutRentLocators.COMMENT_FIELD).send_keys(comment)

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def click_order(self):
        return self.find_element(AboutRentLocators.ORDER_BUTTON).click()

    @allure.step("Кликнуть на кнопку подтверждения заказа - 'Да'")
    def click_yes(self):
        return self.find_element(AboutRentLocators.YES_BUTTON).click()

    @allure.step("Заполнить форму заказа 'Про аренду' и подтвердить заказ")
    def fill_about_rent_form(self, date, number_of_days, color, comment):
        self.choose_date(date)
        self.choose_rental_period(number_of_days)
        self.choose_color(color)
        self.enter_comment(comment)
        self.click_order()
        return self.click_yes()
