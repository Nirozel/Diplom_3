import allure

from pages import main_page
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Открытие деталей заказа")
    def test_open_order_details(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Переход в ленту заказов"):
            main_page.go_to_order_feed()
            order_feed_page.wait_for_feed_page_loaded()

        with allure.step("Клик по заказу"):
            order_feed_page.click_order_detail()

        with allure.step("Проверка отображения состава заказа в модальном окне"):
            assert order_feed_page.order_feed_modal_is_visible()

    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_order_in_feed(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        with allure.step("Создание нового заказа"):
            with allure.step("Добавление булки и оформление заказа"):
                main_page.drag_bun_to_constructor(ingredient_name="Флюоресцентная булка R2-D3")
                main_page.wait_for_page_loaded()
                main_page.place_order()
            with allure.step("Проверка номера заказа"):
                assert main_page.is_order_modal_opened()
                number_order = order_feed_page.get_number_order_details()
                main_page.wait_for_page_loaded()
                main_page.close_order_modal()
        with allure.step("Переход в ленту заказов"):
            main_page.go_to_order_feed()
            order_feed_page.wait_for_feed_page_loaded()

        with allure.step("Получение заказа в ленте"):
            getting_number = order_feed_page.get_order_detail()

            with allure.step("Поиск номера заказа"):
                assert number_order in getting_number

    @allure.title("При создании заказа счетчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter_increase(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_feed_page_loaded()

        with allure.step("Получение начального значения счетчика"):
            main_page.go_to_order_feed()
            main_count = order_feed_page.get_main_count()

        with allure.step("Создание нового заказа"):
            main_page.go_to_constructor()
            main_page.drag_bun_to_constructor(ingredient_name="Флюоресцентная булка R2-D3")
            main_page.wait_for_page_loaded()
            main_page.place_order()

        with allure.step("Проверка номера заказа"):
            assert main_page.is_order_modal_opened()
            number_order = order_feed_page.get_number_order_details()
            order_feed_page.get_number_order_details()
            main_page.wait_for_page_loaded()
            main_page.close_order_modal()
        with allure.step("Переход в ленту заказов"):
            order_feed_page.wait_for_feed_page_loaded()
            main_page.go_to_order_feed()
            order_feed_page.wait_for_feed_page_loaded()
        with allure.step("Получение заказа в ленте"):
            getting_number = order_feed_page.get_order_detail()

            with allure.step("Поиск номера заказа"):
                assert number_order in getting_number

        with allure.step("Проверка увеличения счетчика"):
            new_count = order_feed_page.get_total_orders()
            assert new_count > main_count

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.wait_for_page_loaded()

        with allure.step("Создание нового заказа"):
            main_page.go_to_constructor()
            main_page.drag_bun_to_constructor(ingredient_name="Флюоресцентная булка R2-D3")
            main_page.wait_for_page_loaded()
            main_page.place_order()

        with allure.step("Проверка номера заказа"):
            assert main_page.is_order_modal_opened()
            number_order = order_feed_page.get_number_order_details()
            order_feed_page.get_number_order_details()
            main_page.wait_for_page_loaded()
            main_page.close_order_modal()

        with allure.step("Переход в ленту заказов"):
            main_page.go_to_order_feed()
            order_feed_page.wait_for_feed_page_loaded()

        with allure.step("Проверка раздела 'В работе'"):
            orders_in_progress = order_feed_page.get_order_in_progress()
            assert number_order in orders_in_progress
