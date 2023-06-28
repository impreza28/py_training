import allure
from model.contact import Contact


@allure.epic("Тесты добавления контактов")
@allure.description("Авторизация и добавление нового контакта")
def test_add_contact(app):
    app.contact.open_contact_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(firstname="Lara", middlename="Sergeevna", lastname="Kroft"))
    app.contact.return_to_home_page()
    contact = Contact(firstname="Lara", lastname="Kroft")
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts), "Количество контактов до добавления и после не соответствует"

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"
