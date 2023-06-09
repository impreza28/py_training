import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        with allure.step('Нажать на add new'):
            wd.find_element(By.LINK_TEXT, "add new").click()
        with allure.step('Ввести firstname'):
            wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        with allure.step('Ввести middlename'):
            wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        with allure.step('Ввести lastname'):
            wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        with allure.step('Нажать кнопку Enter'):
            wd.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        with allure.step('Нажать на ссылку open home page'):
            wd.find_element(By.LINK_TEXT, "home page").click()
