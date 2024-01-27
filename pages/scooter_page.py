import allure
from pages.base_page import BasePage


class ScooterPage(BasePage):
    @allure.step("Нажать на вопрос")
    def click_on_question(self, question):
        return self.find_element(question).click()

    @allure.step("Найти на странице ответ на вопрос")
    def check_answer_is_visible(self, answer):
        return self.find_element(answer)

    @allure.step("Получить текст ответа")
    def get_text_of_answer(self, answer):
        return self.find_element(answer).text

    @allure.step("Кликнуть на кнопку заказа самоката")
    def click_on_button_order(self, button):
        return self.find_element(button).click()
