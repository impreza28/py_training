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
    app.contact.modify_contact(new_contact, index, old_contacts[index].id)
    app.contact.return_to_home_page()

    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts), "Количество контактов до добавления и после не соответствует"
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max), "Отсортированные списки не совпадают"
 