from .base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def enter_email(self, email):
        self.input_text(LoginLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.input_text(LoginLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def click_forgot_password_link(self):
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)
