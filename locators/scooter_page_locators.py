from selenium.webdriver.common.by import By


class ScooterPageLocators:
    QUESTION_0 = (By.ID, "accordion__heading-0")  # вопрос №1
    ANSWER_0 = (By.XPATH, "//div[@id='accordion__panel-0']/p")  # ответ №1
    QUESTION_1 = (By.ID, "accordion__heading-1")
    ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    QUESTION_2 = (By.ID, "accordion__heading-2")
    ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    QUESTION_3 = (By.ID, "accordion__heading-3")
    ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    QUESTION_4 = (By.ID, "accordion__heading-4")
    ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    QUESTION_5 = (By.ID, "accordion__heading-5")
    ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    QUESTION_6 = (By.ID, "accordion__heading-6")
    ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    QUESTION_7 = (By.ID, "accordion__heading-7")
    ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-7']/p")

    TEXT_0 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."  # текст ответа №1
    TEXT_1 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    TEXT_2 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    TEXT_3 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    TEXT_4 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    TEXT_5 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    TEXT_6 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    TEXT_7 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
