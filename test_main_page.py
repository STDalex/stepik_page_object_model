from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from resources.text_constants import TextConstants
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():

    @pytest.mark.regression
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.regression
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.cart_guest
class TestCartFromMainPage():

    @pytest.mark.smoke
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser, language):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_cart_empty()
        assert cart_page.should_be_cart_empty_message_text() == TextConstants.get_text(language).EMPTY_BASKET_MESSAGE

