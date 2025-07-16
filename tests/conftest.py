import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import VALID_LOGIN_EMAIL, VALID_LOGIN_PASSWORD, URL


@pytest.fixture(params=["Chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "Chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.go_to_profile()
    login_page.enter_email(VALID_LOGIN_EMAIL)
    login_page.enter_password(VALID_LOGIN_PASSWORD)
    login_page.click_login_button()
