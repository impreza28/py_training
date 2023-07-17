import allure
from model.contact import Contact
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=firstname, lastname=lastname, middlename=middlename)
            for firstname in ["", random_string("firstname", 10)]
            for lastname in ["", random_string("lastname", 10)]
            for middlename in ["", random_string("middlename", 10)]]

@allure.epic("Тесты добавления контактов")
@allure.description("Авторизация и добавление нового контакта")
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact_random(app, contact):

    app.contact.open_contact_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    app.contact.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts), "Количество контактов до добавления и после не соответствует"

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"

@allure.description("Авторизация и добавление нового контакта( из json)")
def test_add_contact_jsondata(app, json_contacts):
    app.contact.open_contact_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(json_contacts)
    app.contact.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts), "Количество контактов до добавления и после не соответствует"

    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"

@allure.description("Авторизация и добавление нового контакта(с БД)")
def test_add_contact_with_db_check(app, json_contacts, db,check_ui):
    app.contact.open_contact_page()
    old_contacts = db.get_contact_list()
    app.contact.create_contact(json_contacts)
    app.contact.return_to_home_page()
    new_contacts = db.get_contact_list()

    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max), "Отсортированные списки не совпадают"
