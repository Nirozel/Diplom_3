from .base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):
    def click_show_password(self):
        self.click_with_modal_handling(
            ResetPasswordLocators.SHOW_PASSWORD_BUTTON,
            ResetPasswordLocators.MODAL_OVERLAY
        )

    def is_password_input_active(self):
        return self.is_visible(ResetPasswordLocators.ACTIVE_PASSWORD_FIELD)

    def is_code_input_visible(self):
        return self.is_visible(ResetPasswordLocators.CODE_INPUT)
