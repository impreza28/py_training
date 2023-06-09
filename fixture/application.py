import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()

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



    def open_home_page(self):
        with allure.step('Открытие страницы addressbook'):
            self.wd.get("http://localhost/addressbook/")
        with allure.step('Открытие окна браузера на полный экран'):
            self.wd.set_window_size(2062, 1126)


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
        self.return_to_groups_page()

    def open_group_page(self):
        with allure.step('Перейти в Группы'):
            self.wd.find_element(By.LINK_TEXT, "groups").click()


