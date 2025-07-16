from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    @allure.step("ждать элемент")
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("проверить кликабельность")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    @allure.step("Ввести текст '{text}'")
    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Видимость элемента")
    def is_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)
        drag_and_drop(self.driver, source, target)

    @staticmethod
    def get_ingredient_locator_by_name(ingredient_name):
        return By.XPATH, f"//img[contains(@alt, '{ingredient_name}')]/ancestor::a[contains(@class, 'BurgerIngredient_ingredient__')]"

    # def click_via_js(self, element):
    #     ActionChains(self.driver).move_to_element(element).click().perform()
    #
    # def click_with_modal_handling(self, locator, modal_overlay_locator=None):
    #     try:
    #         self.click(locator)
    #     except ElementClickInterceptedException:
    #         if modal_overlay_locator:
    #             self.wait_for_element_hide(modal_overlay_locator)
    #         button = self.wait_for_clickable(locator)
    #         self.click_via_js(button)
