from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert#для работы с alert
        alert.accept()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        #символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.


"""main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py"""



