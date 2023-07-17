import random

import allure
from model.contact import Contact
from random import randrange


@allure.epic("Тесты изменения контактов")
@allure.description("Авторизация и изменение первого контакта")
def test_modify_contact(app):
    app.contact.open_contact_page()
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    new_contact = Contact(firstname="New firstname", lastname="New lastname")
    new_contact.id = old_contacts[index].id
    app.contact.select_contact_by_index(index)
    app.contact.modify_contact(new_contact, old_contacts[index].id)
    app.contact.return_to_home_page()

    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts), "Количество контактов до добавления и после не соответствует"
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"


@allure.description("Авторизация и изменение контакта (с БД")
def test_modify_contact(app, db, check_ui):
    app.contact.open_contact_page()
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()

    new_contact = Contact(firstname="New firstname", lastname="New lastname")
    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)

    app.contact.select_contact_by_id(selected_contact.id)
    app.contact.modify_contact(new_contact, selected_contact.id)
    app.contact.return_to_home_page()

    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts), "Количество контактов до добавления и после не соответствует"

    for i in range(len(old_contacts)):
        if old_contacts[i].id == selected_contact.id:
            old_contacts[i].firstname = new_contact.firstname
            old_contacts[i].lastname = new_contact.lastname
            break

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max), "Отсортированные списки не совпадают"

