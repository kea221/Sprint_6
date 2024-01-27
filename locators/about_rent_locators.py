from selenium.webdriver.common.by import By


class AboutRentLocators:
    RENT_HEADER = (By.XPATH, "//div[@class='Order_Header__BZXOb']")  # заголовок "Про аренду"

    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # поле ввода/выбора даты
    CALENDAR = (By.CLASS_NAME, "react-datepicker__month-container")  # выпадающий календарь
    TODAY = (By.XPATH, "//div[contains (@class, 'react-datepicker__day--today')]")  # сегодняшний день в календаре
    # первый день следующей недели (считая от сегодняшнего дня)
    OTHER_DAY = (By.XPATH, "//div[contains (@class, 'react-datepicker__day--today')]/parent::div/following-sibling::div/div")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-placeholder")  # поле выбора срока аренды
    RENTAL_PERIOD_MENU = (By.CLASS_NAME, "Dropdown-menu")  # выпадушка со сроками аренды
    NUMBER_OF_DAYS_3 = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")  # трое суток
    NUMBER_OF_DAYS_1 = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")  # сутки

    BLACK = (By.XPATH, "//label[@for='black']")  # цвет самоката - чёрный
    GREY = (By.XPATH, "//label[@for='grey']")  # цвет самоката - серый

    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # поле ввода комментария

    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # кнопка Заказать
    MODAL_ORDER = (By.CLASS_NAME, "Order_Modal__YZ-d3")  # модальное окно "Хотите оформить заказ?"
    YES_BUTTON = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']//button[text()='Да']")  # кнопка Да
    # текст в модалке "Заказ оформлен"
    MODAL_SUCCESS = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
