import allure
from pages.main_page import MainPage


class TestMainFunctionality:
    @allure.title('Переход в конструктор')
    def test_go_to_constructor(self, driver):
        with allure.step('Перейти на страницу ленты заказов'):
            main_page = MainPage(driver)
            main_page.go_to_order_feed()

        with allure.step('Кликнуть на ссылку конструктора'):
            main_page.go_to_constructor()

        with allure.step('Проверить URL главной страницы'):
            assert "stellarburgers.nomoreparties.site" in driver.current_url
            assert "feed" not in driver.current_url

    @allure.title('Переход в ленту заказов')
    def test_go_to_order_feed(self, driver):
        with allure.step('Кликнуть на ссылку ленты заказов'):
            main_page = MainPage(driver)
            main_page.go_to_order_feed()

        with allure.step('Проверить URL ленты заказов'):
            assert "feed" in driver.current_url

    @allure.title('Открытие и закрытие модального окна ингредиента')
    def test_ingredient_modal(self, driver):
        with allure.step('Открыть модальное окно ингредиента'):
            main_page = MainPage(driver)
            main_page.open_ingredient_details()

        with allure.step('Проверить видимость модального окна'):
            assert main_page.is_ingredient_modal_visible()

        with allure.step('Закрыть модальное окно'):
            main_page.close_ingredient_modal()

        with allure.step('Проверить отсутствие модального окна'):
            assert main_page.is_ingredient_modal_hide()

    @allure.title('Изменение счетчика')
    def test_place_order(self, driver):
        with allure.step('Получить начальное значение счетчика'):
            main_page = MainPage(driver)
            initial_counter = main_page.get_ingredient_counter()
            main_page.drag_bun_to_constructor(ingredient_name="Флюоресцентная булка R2-D3")

        with allure.step('Проверить увеличение счетчика'):
            assert main_page.get_ingredient_counter() > initial_counter

    @allure.title("Оформление заказа авторизованным пользователем")
    def test_place_order(self, driver, login):
        main_page = MainPage(driver)

        with allure.step("Добавление булки и оформление заказа"):
            main_page.drag_bun_to_constructor(ingredient_name="Флюоресцентная булка R2-D3")
            main_page.place_order()

        with allure.step("Проверка номера заказа"):
            assert main_page.is_order_modal_opened()
