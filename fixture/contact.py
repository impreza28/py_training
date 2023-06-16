import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from model import contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        with allure.step('Нажать на add new'):
            wd.find_element(By.LINK_TEXT, "add new").click()
        self.contact_fields_filling(contact)
        with allure.step('Нажать кнопку Enter'):
            wd.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()

    def contact_fields_filling(self, contact):
        wd = self.app.wd
        with allure.step('Ввести firstname'):
            wd.find_element(By.NAME, "firstname").clear()
            wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        with allure.step('Ввести middlename'):
            wd.find_element(By.NAME, "middlename").clear()
            wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        with allure.step('Ввести lastname'):
            wd.find_element(By.NAME, "lastname").clear()
            wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)

    def return_to_home_page(self):
        wd = self.app.wd
        with allure.step('Нажать на ссылку open home page'):
            wd.find_element(By.LINK_TEXT, "home page").click()

    def select_first_contact(self):
        wd = self.app.wd
        with allure.step('Выбрать первый контакт'):
            wd.find_element(By.NAME, "selected[]").click()

    def delete_contact(self):
        wd = self.app.wd
        with allure.step('Нажать кнопку Delete'):
            wd.find_element(By.XPATH, "(//input[@value=\'Delete\'])").click()
        with allure.step('Нажать кнопку ОК в сообщении "Delete 1 addresses?"'):
            wd.switch_to.alert.accept()
    def modify_contact(self, contact):
        wd = self.app.wd
        with allure.step('Выбрать первый контакт'):
            wd.find_element(By.XPATH, "//img[@alt=\'Edit\']").click()
        self.contact_fields_filling(contact)
        with allure.step('Нажать кнопку Update'):
            wd.find_element(By.XPATH, "(//input[@name=\'update\'])").click()
    def open_contact_page(self):
        wd = self.app.wd
        with allure.step('Нажать на ссылку Home для перехода на главную страницу'):
            wd.find_element(By.LINK_TEXT, "home").click()


