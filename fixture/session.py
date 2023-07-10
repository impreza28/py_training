import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        with allure.step('Ввести логин'):
            wd.find_element(By.NAME, "user").clear()
            wd.find_element(By.NAME, "user").send_keys(username)
        with allure.step('Ввести пароль'):
            wd.find_element(By.NAME, "pass").clear()
            wd.find_element(By.NAME, "pass").send_keys(password)
        with allure.step('Нажать кнопку Login'):
            wd.find_element(By.XPATH, '//input[@value="Login"]').click()

    def logout(self):
        wd = self.app.wd
        with allure.step('Нажать на ссылку Logout'):
            wd.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.NAME, "user"))
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        user = self.get_logged_user()
        return user == username

    def get_logged_user(self):
        wd = self.app.wd
        user = wd.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]
        return user

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)





