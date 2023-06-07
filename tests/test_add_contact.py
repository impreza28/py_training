import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

from contact import Contact


@allure.epic("Тесты добавления контактов")
class TestAddContact():
    def setup_method(self):
        self.wd = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self):
        self.wd.quit()

    @allure.description("Авторизация и добавление нового контакта")
    def test_add_contact(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="Lara", middlename="Sergeevna", lastname="Kroft"))
        self.return_to_home_page()

    def return_to_home_page(self):
        with allure.step('Нажать на ссылку open home page'):
            self.wd.find_element(By.LINK_TEXT, "home page").click()

    def create_contact(self, contact):
        with allure.step('Нажать на add new'):
            self.wd.find_element(By.LINK_TEXT, "add new").click()
        with allure.step('Ввести firstname'):
            self.wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        with allure.step('Ввести middlename'):
            self.wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        with allure.step('Ввести lastname'):
            self.wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        with allure.step('Нажать кнопку Enter'):
            self.wd.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()

    def login(self, username, password):
        with allure.step('Ввести логин'):
            self.wd.find_element(By.NAME, "user").send_keys(username)
        with allure.step('Ввести пароль'):
            self.wd.find_element(By.NAME, "pass").send_keys(password)
        with allure.step('Нажать кнопку Login'):
            self.wd.find_element(By.XPATH, "//input[@value=\'Login\']").click()

    def open_home_page(self):
        with allure.step('Открытие страницы addressbook'):
            self.wd.get("http://localhost/addressbook/")
        with allure.step('Открытие окна браузера на полный экран'):
            self.wd.set_window_size(2062, 1126)
