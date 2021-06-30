from selenium.webdriver.common.by import By


class MainPageLocators():  # создали новый класс
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # теперь каждый селектор — это пара: как искать и что искать. Наш селектор находится в переменной LOGIN_LINK


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')


class ProductPageLocators():
    ADD_BASKET = (By.XPATH, '//form[@id="add_to_basket_form"]')
    PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    SUM_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_NAME_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')

"""locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать"""