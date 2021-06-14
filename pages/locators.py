from selenium.webdriver.common.by import By


class MainPageLocators():#создали новый класс
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")#теперь каждый селектор — это пара: как искать и что искать. Наш селектор находится в переменной LOGIN_LINK

class LoginPageLocators():
    