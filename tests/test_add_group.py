import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from group import Group


@allure.epic("Тесты добавления группы")
class TestAddGroup():
    def setup_method(self):
        self.wd = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self):
        self.wd.quit()

    @allure.description("Авторизация и добавление новой группы")
    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(Group(name="Группа1", header="header1", footer="footer2"))
        self.return_to_groups_page()
        self.logout()

    @allure.description("Авторизация и добавление новой группы без данных")
    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(Group(name="", header="", footer=""))
        self.return_to_groups_page()
        self.logout()

    def logout(self):
        with allure.step('Нажать на ссылку Logout'):
            self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        with allure.step('Нажать на ссылку group page для возврата в список групп'):
            self.wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        with allure.step('Нажать на кнопку New group'):
            self.wd.find_element(By.NAME, "new").click()
        with allure.step('Ввести group_name'):
            self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        with allure.step('Ввести group_header'):
            self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        with allure.step('Ввести group_footer'):
            self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        with allure.step('Нажать кнопку Enter information'):
            self.wd.find_element(By.NAME, "submit").click()

    def open_group_page(self):
        with allure.step('Перейти в Группы'):
            self.wd.find_element(By.LINK_TEXT, "groups").click()

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
