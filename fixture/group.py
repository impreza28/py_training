import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
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

    def open_group_page(self):
        wd = self.app.wd
        with allure.step('Перейти в Группы'):
            wd.find_element(By.LINK_TEXT, "groups").click()