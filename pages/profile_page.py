from .base_page import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):
    def click_order_history_button(self):
        self.click(ProfileLocators.ORDER_HISTORY_LINK)

    def click_logout_button(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)

    def is_save_button_visible(self):
        return self.is_visible(ProfileLocators.SAVE_BUTTON)

    def is_order_history_page(self):
        current_url = self.get_current_url()
        return "account/order-history" in current_url
