from locators.scooter_page_locators import ScooterPageLocators
from locators.order_for_who_locators import OrderForWhoLocators
from locators.about_rent_locators import AboutRentLocators


class Constants:
    variables = [
        (ScooterPageLocators.QUESTION_0, ScooterPageLocators.ANSWER_0, ScooterPageLocators.TEXT_0),
        (ScooterPageLocators.QUESTION_1, ScooterPageLocators.ANSWER_1, ScooterPageLocators.TEXT_1),
        (ScooterPageLocators.QUESTION_2, ScooterPageLocators.ANSWER_2, ScooterPageLocators.TEXT_2),
        (ScooterPageLocators.QUESTION_3, ScooterPageLocators.ANSWER_3, ScooterPageLocators.TEXT_3),
        (ScooterPageLocators.QUESTION_4, ScooterPageLocators.ANSWER_4, ScooterPageLocators.TEXT_4),
        (ScooterPageLocators.QUESTION_5, ScooterPageLocators.ANSWER_5, ScooterPageLocators.TEXT_5),
        (ScooterPageLocators.QUESTION_6, ScooterPageLocators.ANSWER_6, ScooterPageLocators.TEXT_6),
        (ScooterPageLocators.QUESTION_7, ScooterPageLocators.ANSWER_7, ScooterPageLocators.TEXT_7)
    ]

    questions = [ScooterPageLocators.QUESTION_0, ScooterPageLocators.QUESTION_1, ScooterPageLocators.QUESTION_2,
                 ScooterPageLocators.QUESTION_3, ScooterPageLocators.QUESTION_4, ScooterPageLocators.QUESTION_5,
                 ScooterPageLocators.QUESTION_6, ScooterPageLocators.QUESTION_7]

    answers = [ScooterPageLocators.ANSWER_0, ScooterPageLocators.ANSWER_1, ScooterPageLocators.ANSWER_2,
               ScooterPageLocators.ANSWER_3, ScooterPageLocators.ANSWER_4, ScooterPageLocators.ANSWER_5,
               ScooterPageLocators.ANSWER_6, ScooterPageLocators.ANSWER_7]

    order_form = [("Саша", "Пушкин", "Ивантеевская улица, 17к1", OrderForWhoLocators.STATION_1, "89505557896"),
                  ("Антоша", "Чехонте", "Фролов переулок, 2", OrderForWhoLocators.STATION_8, "89991234567")]

    about_rent = [(AboutRentLocators.DATE_1, AboutRentLocators.NUMBER_OF_DAYS_3, AboutRentLocators.BLACK, "Комментарий для курьера"),
                  (AboutRentLocators.DATE_2, AboutRentLocators.NUMBER_OF_DAYS_1, AboutRentLocators.GREY, "")]
