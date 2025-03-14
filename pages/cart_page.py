from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_be_cart_empty(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "Cart is not empty"

    def should_be_cart_empty_message_text(self):
        return self.element_text(*CartPageLocators.EMPTY_BASKET_MESSAGE)
