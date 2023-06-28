import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from model.contact import Contact
from selenium.webdriver.support.wait import WebDriverWait


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
        if contact.firstname is not None:
            with allure.step('Ввести firstname'):
                wd.find_element(By.NAME, "firstname").clear()
                wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        if contact.middlename is not None:
            with allure.step('Ввести middlename'):
                wd.find_element(By.NAME, "middlename").clear()
                wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        if contact.lastname is not None:
            with allure.step('Ввести lastname'):
                wd.find_element(By.NAME, "lastname").clear()
                wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)

    def return_to_home_page(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//input[@value=\'Delete\']")) > 0 and len(
                wd.find_elements(By.XPATH, "//input[@value=\'Send e-Mail\']")) > 0:
            return
        with allure.step('Нажать на ссылку open home page'):
            wd.find_element(By.LINK_TEXT, "home page").click()
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.ID, "maintable"))

    def select_first_contact(self):
        wd = self.app.wd
        with allure.step('Выбрать первый контакт'):
            wd.find_element(By.NAME, "selected[]").click()

    def delete_contact(self):
        wd = self.app.wd
        with allure.step('Нажать кнопку Delete'):
            wd.find_element(By.XPATH, "//input[@value=\'Delete\']").click()
        with allure.step('Нажать кнопку ОК в сообщении "Delete 1 addresses?"'):
            wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.ID, "maintable"))

    def modify_contact(self, contact):
        wd = self.app.wd
        with allure.step('Выбрать первый контакт'):
            wd.find_element(By.XPATH, "//img[@alt=\'Edit\']").click()
        self.contact_fields_filling(contact)
        with allure.step('Нажать кнопку Update'):
            wd.find_element(By.XPATH, "//input[@name=\'update\']").click()

    def open_contact_page(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//input[@value=\'Delete\']")) > 0 and len(
                wd.find_elements(By.XPATH, "//input[@value=\'Send e-Mail\']")) > 0:
            return
        with allure.step('Нажать на ссылку Home для перехода на главную страницу'):
            wd.find_element(By.LINK_TEXT, "home").click()

    def count_contacts(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        list_contacts = []
        m = 1
        for element in wd.find_elements(By.NAME, "entry"):
            text = element.text
            #firstname = element.find_element(By.XPATH, f"//[@id=\"maintable\"]/tbody/tr[{m + 1}]/td[3]").text
            #lastname = element.find_element(By.XPATH, f"//[@id=\"maintable\"]/tbody/tr[{m + 1}]/td[2]").text
            lastname = wd.find_element(By.CSS_SELECTOR, f"tr:nth-child({m+1}) > td:nth-child(2)").text
            firstname = wd.find_element(By.CSS_SELECTOR, f"tr:nth-child({m+1}) > td:nth-child(3)").text
            id = element.find_element(By.NAME, "selected[]").get_attribute("value")
            # list_contact.append(Contact(contact_row=text, id=id))
            list_contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
            m += 1
            # maintable > tbody > tr:nth-child(2) > td:nth-child(2)
            # maintable > tbody > tr.odd > td:nth-child(2)

        return list_contacts

    # for element in wd.find_elements(By.NAME, "entry"):
    #    firstname = element.find_element(By.XPATH, "//*[@id=\'maintable\']/tbody/tr/td[2]").text
    #    lastname = element.find_element(By.XPATH, "//*[@id=\'maintable\']/tbody/tr/td[3]").text
    #    id = element.find_element(By.XPATH, "//input[@id]").get_attribute("value")
    #     list_contact.append(Contact(firstname=firstname, lastname=lastname, id=id))
    # return list_contact

    # def get_group_list(self):
    #    wd = self.app.wd
    #    self.open_group_page()
    #   list_group = []
    #    for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
    #       text = element.text
    #        id = element.find_element(By.NAME, "selected[]").get_attribute("value")
    #        list_group.append(Group(name=text, id=id))
    #    return list_group
