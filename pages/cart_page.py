from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_be_cart_empty(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS), \
            "Cart is not empty, but should be"

    def should_be_cart_empty_message_text(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not present"
        return self.browser.find_element(*CartPageLocators.EMPTY_BASKET_MESSAGE).text
