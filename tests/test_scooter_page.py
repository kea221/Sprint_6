import pytest
import allure
from constants import Constants
from locators.scooter_page_locators import ScooterPageLocators
from pages.scooter_page import ScooterPage


class Test:
    @allure.title("Проверяем, что после клика на вопрос открывается соответствующий ответ")
    @pytest.mark.parametrize('question,answer,text', Constants.variables)
    def test_answer_got(self, driver_with_scroll, question, answer, text):
        scooter_page = ScooterPage(driver_with_scroll)
        scooter_page.click_on_cookie_button()
        scooter_page.click_on_question(question)
        scooter_page.check_answer_is_visible(answer)
        actual_text = scooter_page.get_text_of_answer(answer)
        assert actual_text == text
