from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "add to basket button is not presented"

    def good_added_to_basket(self):
        good_added_message = self.is_element_present(*ProductPageLocators.GOOD_ADDED_MESSAGE)
        good_name = ProductPageLocators.GOOD_NAME  # название товара (кортеж значений)
        good_name_message = ProductPageLocators.GOOD_NAME_MESSAGE  # название товара в сообщении (кортеж значений)
        assert good_added_message, "message about good added is not presented"
        assert self.found_element(*good_name).text == self.found_element(*good_name_message).text, \
            "Product name does not match the product added "
        print(self.found_element(*ProductPageLocators.GOOD_ADDED_MESSAGE).text)

    def basket_value(self):
        price = ProductPageLocators.PRICE_VALUE  # стоимость товара (кортеж значений)
        b_value = ProductPageLocators.BASKET_VALUE_MESSAGE  # стоимость содержимого корзины (кортеж значений)
        assert self.is_element_present(*b_value), "message with basket value is not presented"
        assert self.found_element(*b_value).text == self.found_element(*price).text, \
            "The price of the cart does not match the price of the product"
        print(self.found_element(*ProductPageLocators.BASKET_FULL_MESSAGE).text)
