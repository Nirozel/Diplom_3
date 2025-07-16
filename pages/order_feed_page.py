from locators.main_page_locators import MainPageLocators
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    def wait_for_feed_page_loaded(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    def click_order_detail(self):
        self.click(OrderFeedLocators.ORDER_ITEM)

    def order_feed_modal_is_visible(self):
        return self.is_visible(OrderFeedLocators.ORDER_MODAL_COMPOSITION)
