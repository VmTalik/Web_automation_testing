from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def no_goods_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.GOODS_IN_BASKET_HEADER), \
            "Goods are already in the basket !"

    def basket_is_empty_message(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY), "There is no text that the cart is empty!"
