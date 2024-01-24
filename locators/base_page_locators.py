from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # кнопка принятия куки
    ORDER_BUTTON_IN_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    LOGO_SAMOKAT = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    LOGO_DZEN = (By.XPATH, "//a[@class='desktop-base-header__logoLink-aE']")
