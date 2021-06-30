from pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()





"""Принцип работы test_main_page.py
   1.выдаём нужный для проверки линк
   2.созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
   3.следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
   4.добавляем проверки, которые создавали методами в main_page.py"""
