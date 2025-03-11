from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._product_name = None
        self._product_price = None
    
    def add_to_cart(self):
        # Сохраняем имя и цену товара до добавления в корзину
        self._product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self._product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Добавляем в корзину
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()


    def should_be_same_product_name(self):
        # Проверяем, что имя товара было сохранено
        assert self._product_name is not None, "Product name was not saved before adding to cart"
        # Получаем текст названия товара из алерта
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        # Сравниваем с сохраненным названием
        assert self._product_name == product_name_in_alert, \
            f"Product name in alert '{product_name_in_alert}' does not match product name '{self._product_name}' on the page"

    def should_be_same_price(self):
        # Проверяем, что цена товара была сохранена
        assert self._product_price is not None, "Product price was not saved before adding to cart"
        # Получаем текст цены товара из алерта
        price_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT).text
        # Сравниваем с сохраненной ценой
        assert self._product_price == price_in_alert, \
            f"Product price in alert '{price_in_alert}' does not match price '{self._product_price}' on the page"





