import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new"))>0:
            return
        with allure.step('Нажать на ссылку group page для возврата в список групп'):
            wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        wd = self.app.wd
        with allure.step('Нажать на кнопку New group'):
            wd.find_element(By.NAME, "new").click()
        with allure.step('Ввести group_name'):
            wd.find_element(By.NAME, "group_name").send_keys(group.name)
        with allure.step('Ввести group_header'):
            wd.find_element(By.NAME, "group_header").send_keys(group.header)
        with allure.step('Ввести group_footer'):
            wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        with allure.step('Нажать кнопку Enter information'):
            wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache= None

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new"))>0:
            return
        with allure.step('Перейти в Группы'):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        with allure.step('Перейти в Группы'):
            wd.find_element(By.LINK_TEXT, "groups").click()
        with allure.step('Выбрать группу'):
            wd.find_element(By.NAME, "selected[]").click()
        with allure.step('Нажать кнопку Delete group'):
            wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        with allure.step('Выбрать группу'):
            wd = self.app.wd
            wd.find_element(By.NAME, "selected[]").click()

    def modify_group(self, group):
        wd = self.app.wd
        with allure.step('Нажать на кнопку Edit group'):
            wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        with allure.step('Нажать кнопку Update'):
            wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            with allure.step(f'Ввести {field_name}'):
                wd.find_element(By.NAME, field_name).clear()
                wd.find_element(By.NAME, field_name).send_keys(text)

    def count_groups(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))

    group_cache = None
    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)






