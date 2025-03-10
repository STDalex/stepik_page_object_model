from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверяем, что текущий URL содержит подстроку "/login/"
        try:
            WebDriverWait(self.browser, 10).until(
                EC.url_contains("/login/")
            )
        except TimeoutException:
            current_url = self.browser.current_url
            assert False, f"Login URL is incorrect. Expected '/login/' to be in {current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"