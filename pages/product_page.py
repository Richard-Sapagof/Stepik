from pages.base_page import BasePage
from pages.locators import ProductPageLocators





class ProductPage(BasePage):
    def add_product_in_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        link.click()
        #self.solve_quiz_and_get_code() #подтянули метод для решения alert

    def should_sum_in_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        sum_basket = self.browser.find_element(*ProductPageLocators.SUM_IN_BASKET).text
        assert book_price == sum_basket, "Sum basket is not presented"


    def should_text_book(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_in_alert = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT).text
        assert book_name == book_name_in_alert, "Name book is not presented"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),  \
            "Success message is presented, but should not be"

    def should_disappered(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"



