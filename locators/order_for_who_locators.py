from selenium.webdriver.common.by import By


class OrderForWhoLocators:

    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")  # поле для ввода Имени
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")  # поле для ввода Фамилии
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # поле для ввода Адреса
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")  # список станций метро
    # станция метро №1 Бульвар Рокоссовского
    STATION_1 = (By.XPATH, "//button[@class='Order_SelectOption__82bhS select-search__option' and @value='1']")
    # станция метро №8 Чистые пруды
    STATION_8 = (By.XPATH, "//button[@class='Order_SelectOption__82bhS select-search__option' and @value='8']")
    # поле для ввода Номера телефона
    NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    BUTTON_GO = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # кнопка Далее

    RENT_HEADER = (By.XPATH, "//div[@class='Order_Header__BZXOb']")  # заголовок "Про аренду" на второй форме заказа
