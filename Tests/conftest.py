import pytest
from Configs.config import TestData
from selenium import webdriver
from Pages.homePage import HomePage


@pytest.fixture()
def driver():
    d = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    d.maximize_window()
    d.get(TestData.BASE_URL)
    yield d
    d.quit()


@pytest.fixture()
def homepage(driver):
    return HomePage(driver)
