from selenium.webdriver.common.by import By


class OrderFeedLocators:
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_ITEM = (By.CSS_SELECTOR, "li[class*='OrderHistory_listItem']")
    ORDER_MODAL_COMPOSITION =(By.XPATH, "//p[@class='text text_type_main-medium mb-8' and text()='Cостав']")
    NUMBERS_IN_FEED = (By.XPATH, '//*[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    ORDER_NUMBERS_IN_FEED = (By.XPATH, "//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    TOTAL_ORDERS = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDERS_IN_PROGRESS = (By.XPATH, '//*[contains(@class, "OrderFeed_orderListReady__1YFem") and contains(@class, "OrderFeed_orderList__cBvyi")]')
    CLOSE_MODAL_ORDER = (By.XPATH, '//*[contains(@class, "Modal_modal__close_modified__3V5XS") and contains(@class, "Modal_modal__close__TnseK")]')
