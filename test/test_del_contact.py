import allure
from model.contact import Contact
import random
from random import randrange

@allure.epic("Тесты удаления контактов")
@allure.description("Авторизация и удаление первого контакта")
def test_delete_contact(app):

    app.contact.open_contact_page()

    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.select_contact_by_index(index)
    app.contact.delete_contact()

    new_contacts = app.contact.get_contact_list()

    assert (len(old_contacts)-1) == len(new_contacts), "Количество контактов не совпадает"

    old_contacts.pop(index)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"
@allure.description("Авторизация и удаление контакта (c БД)")
def test_delete_contact_with_db_check(app, db, check_ui):

    app.contact.open_contact_page()

    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()

    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    app.contact.select_contact_by_id(selected_contact.id)
    app.contact.delete_contact()

    new_contacts = db.get_contact_list()

    assert (len(old_contacts)-1) == len(new_contacts), "Количество контактов не совпадает"

    old_contacts.remove(selected_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max), "Отсортированные списки не совпадают"
