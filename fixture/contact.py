import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from model.contact import Contact
from selenium.webdriver.support.wait import WebDriverWait
import re


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
        self.contact_cache = None

    def contact_fields_filling(self, contact):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.XPATH, "//form[@action=\'edit.php\']"))
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
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        with allure.step(f'Выбрать контакт с индексом {index}'):
            wd.find_elements(By.NAME, "selected[]")[index].click()
            # WebDriverWait(wd, 30).until(lambda x: x.find_element(By.NAME, "selected[]")[index].is_selected())
    def select_contact_by_id(self, id):
        wd = self.app.wd
        with allure.step(f'Выбрать контакт с id= {id}'):
            wd.find_element(By.ID, f"{id}").click()
            # WebDriverWait(wd, 30).until(lambda x: x.find_element(By.NAME, "selected[]")[index].is_selected())

    def delete_contact(self):
        wd = self.app.wd
        with allure.step('Нажать кнопку Delete'):
            wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        with allure.step('Нажать кнопку ОК в сообщении "Delete 1 addresses?"'):
            wd.switch_to.alert.accept()
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, ".msgbox"))
        self.contact_cache = None

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        row = wd.find_elements(By.NAME,"entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.XPATH, "//form[@action='edit.php']"))


    def modify_contact(self, contact, id_contact):
        wd = self.app.wd
        with allure.step('У выбранного контакта нажать Edit'):
            wd.find_element(By.XPATH, f"//a[@href='edit.php?id={id_contact}']").click()
        self.contact_fields_filling(contact)
        with allure.step('Нажать кнопку Update'):
            wd.find_element(By.XPATH, "//input[@name='update']").click()
        self.contact_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//input[@value='Delete']")) > 0 and len(
                wd.find_elements(By.XPATH, "//input[@value='Send e-Mail']")) > 0:
            return
        with allure.step('Нажать на ссылку Home для перехода на главную страницу'):
            wd.find_element(By.LINK_TEXT, "home").click()


    def count_contacts(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:

            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            m = 1
            for element in wd.find_elements(By.NAME, "entry"):
                lastname = wd.find_element(By.CSS_SELECTOR, f"tr:nth-child({m + 1}) > td:nth-child(2)").text
                firstname = wd.find_element(By.CSS_SELECTOR, f"tr:nth-child({m + 1}) > td:nth-child(3)").text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                allphones = wd.find_element(By.CSS_SELECTOR, f"tr:nth-child({m + 1}) > td:nth-child(6)").text
                all_emails = wd.find_element(By.CSS_SELECTOR, f"tr:nth-child({m + 1}) > td:nth-child(5)").text
                address = wd.find_element(By.CSS_SELECTOR, f"tr:nth-child({m + 1}) > td:nth-child(4)").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=allphones,
                                                  all_emails_from_home_page=all_emails, address=address))
                m += 1
        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit_by_index(index)

        firstname = wd.find_element(By.NAME,"firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME,"lastname").get_attribute("value")
        id = wd.find_element(By.NAME,"id").get_attribute("value")
        address = wd.find_element(By.NAME,"address").text
        homephone = wd.find_element(By.NAME,"home").get_attribute("value")
        mobilephone = wd.find_element(By.NAME,"mobile").get_attribute("value")
        workphone = wd.find_element(By.NAME,"work").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME,"phone2").get_attribute("value")
        email = wd.find_element(By.NAME,"email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3, address=address)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        with allure.step('Открыть подробную информацию о контакте'):
            self.open_contact_page()
            wd = self.app.wd
            row = wd.find_elements(By.NAME, "entry")[index]
            cell = row.find_elements(By.TAG_NAME, "td")[6]
            cell.find_element(By.TAG_NAME, "a").click()
            WebDriverWait(wd, 10).until(lambda x: x.find_element(By.ID, "content"))

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID,"content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)

        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)


