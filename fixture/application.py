import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        with allure.step('Открытие страницы addressbook'):
            self.wd.get("http://localhost/addressbook/")
        with allure.step('Открытие окна браузера на полный экран'):
            self.wd.set_window_size(2062, 1126)





