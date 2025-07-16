from locators.main_page_locators import MainPageLocators
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    def wait_for_feed_page_loaded(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    def click_order_detail(self):
        self.click(OrderFeedLocators.ORDER_ITEM)

    def get_order_detail(self):
        return self.find_element(OrderFeedLocators.ORDER_ITEM).text

    def order_feed_modal_is_visible(self):
        return self.is_visible(OrderFeedLocators.ORDER_MODAL_COMPOSITION)

    def get_number_order_details(self):
        while True:
            get_number_order = self.find_element(OrderFeedLocators.ORDER_NUMBERS_IN_FEED, timeout=15).text
            if get_number_order != "9999":
                return get_number_order

    def get_main_count(self):
        return self.find_element(OrderFeedLocators.NUMBERS_IN_FEED).text

    def get_total_orders(self):
        return self.find_element(OrderFeedLocators.NUMBERS_IN_FEED).text

    def get_order_in_progress(self, timeout=10):
        while True:
            get_orders = self.wait_for_element(OrderFeedLocators.ORDERS_IN_PROGRESS, timeout).text
            if get_orders != "Все текущие заказы готовы!":
                return get_orders
