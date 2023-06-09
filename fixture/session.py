import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        with allure.step('Ввести логин'):
            wd.find_element(By.NAME, "user").send_keys(username)
        with allure.step('Ввести пароль'):
            wd.find_element(By.NAME, "pass").send_keys(password)
        with allure.step('Нажать кнопку Login'):
            wd.find_element(By.XPATH, "//input[@value=\'Login\']").click()

    def logout(self):
        wd = self.app.wd
        with allure.step('Нажать на ссылку Logout'):
            wd.find_element(By.LINK_TEXT, "Logout").click()
