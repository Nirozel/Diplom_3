import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfile:
    def test_go_to_profile(self, driver, login):
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)
        main_page.wait_for_page_loaded()
        with allure.step("Переход на страницу 'Профиль'"):
            main_page.go_to_profile()
        with allure.step("Проверка перехода в личный кабинет"):
            main_page.wait_for_page_loaded()
            assert profile_page.is_save_button_visible()

    def test_go_to_orders_history(self, driver, login):
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)
        main_page.wait_for_page_loaded()
        with allure.step("Переход на страницу 'Профиль'"):
            main_page.go_to_profile()
            main_page.wait_for_page_loaded()
        with allure.step("Переход на странцу 'История заказов'"):
            profile_page.click_order_history_link()
        with allure.step("Проверка перехода в Историю"):
            assert "account/order-history" in driver.current_url

    def test_logout(self, driver, login):
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)
        main_page.wait_for_page_loaded()
        with allure.step("Переход на страницу 'Профиль'"):
            main_page.go_to_profile()
            main_page.wait_for_page_loaded()
            with allure.step("Тап по кнопку 'Выход'"):
                profile_page.click_logout_button()
        with allure.step("Проверка отображения кнопки 'Войти'"):
            assert main_page.is_login_button_visible()

