import allure
from model.contact import Contact
from model.group import Group
import random
from random import randrange


def test_add_contact_in_group(app, db):
    app.contact.open_contact_page()

    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()
    if len(db.get_group_list()) == 0:
        app.group.open_group_page()
        app.group.create_group(Group(name="name группа", header="header группа", footer="footer группа"))

    #выбрать контакт
    selected_contact = random.choice(app.contact.get_contact_list())
    #отметить чекбокс контакта
    app.contact.select_contact_by_id(selected_contact.id)
    #выбрать группу
    selected_group = random.choice(db.get_group_list())
    #выбрать группу для добавления контакта
    app.contact.select_group_for_add_contact(selected_group.id)
    #добавить контакт в группу
    app.contact.add_contact_to_group()
    #открыть группу с контактом
    app.contact.open_group_page_with_contacts(selected_group.id)

    #проверить добавления контакта в группу через БД
    contact_in_group = db.get_contact_in_group_by_id(selected_group.id, selected_contact.id)
    assert str(contact_in_group[0]) == selected_contact.id and str(contact_in_group[1]) == selected_group.id, "Контакт не добавлен в группу"

    # отметить чекбокс контакта
    app.contact.select_contact_by_id(selected_contact.id)
    # удалить контакт из группы
    app.group.del_contact_from_group()

    # проверить удаление контакта из группы через БД
    contact_in_group = db.get_contact_in_group_by_id(selected_group.id, selected_contact.id)
    assert len(contact_in_group) == 0, "Контакт не удален из группы"
