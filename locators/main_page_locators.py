from selenium.webdriver.common.by import By


class MainPageLocators:
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    INGREDIENT_BUN = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    INGREDIENT_SAUCE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    INGREDIENT_TOPPING = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa7f']")
    INGREDIENT_BUN_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//div[contains(@class, 'counter_counter')]")
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    CONSTRUCTOR_DROP = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_ID_TITLE = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='идентификатор заказа']")


