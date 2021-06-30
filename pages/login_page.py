from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.current_url# реализует проверку на корректный url адрес. Возвращает текущий url
        assert'login' in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)#реализует проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)#реализует проверку, что есть форма регистрации на странице
