from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.login_locators import LoginLocators


class MainPage(BasePage):

    def wait_for_page_loaded(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def go_to_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def go_to_profile(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def open_ingredient_details(self):
        self.click(MainPageLocators.INGREDIENT_BUN)

    def close_ingredient_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    def is_ingredient_modal_hide(self):
        return self.wait_for_element_hide(MainPageLocators.INGREDIENT_MODAL)

    def is_ingredient_modal_visible(self):
        return self.is_visible(MainPageLocators.INGREDIENT_MODAL)

    def get_ingredient_counter(self):
        counter = self.wait_for_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text) if counter.text else 0

    def place_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    def drag_bun_to_constructor(self, ingredient_name):
        ingredient_locator = self.get_ingredient_locator_by_name(ingredient_name)

        self.wait_for_element(ingredient_locator)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_DROP)
        self.drag_and_drop_element(ingredient_locator, MainPageLocators.CONSTRUCTOR_DROP)

    def is_order_modal_opened(self):
        return self.is_visible(MainPageLocators.ORDER_ID_TITLE)

    def is_login_button_visible(self):
        return self.is_visible(LoginLocators.LOGIN_BUTTON)

    def safely_click_order_feed_button(self):
        self.safe_click_with_modal_handling(
            MainPageLocators.ORDER_FEED_BUTTON,
            MainPageLocators.MODAL_OVERLAY
        )

