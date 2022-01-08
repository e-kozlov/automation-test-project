import pytest
from selenium.webdriver.common.by import By
from Support.general_functionality import GeneralFunctionality


class TestQuickView:
    def test_one(self, homepage):
        homepage.find()
