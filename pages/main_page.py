from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_cart_page(self):
        cart_link = self.browser.find_element(*MainPageLocators.CART_LINK)
        cart_link.click()

