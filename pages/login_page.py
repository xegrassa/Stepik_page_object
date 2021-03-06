from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, "url is not 'login' part"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FOR_REGISTRATION)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FOR_REGISTRATION)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FOR_REGISTRATION)
        registration_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        login_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        registration_button.click()
