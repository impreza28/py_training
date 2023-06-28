import allure
from model.contact import Contact

@allure.epic("Тесты удаления контактов")
@allure.description("Авторизация и удаление первого контакта")
def test_delete_contact(app):

    app.contact.open_contact_page()

    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()

    old_contacts = app.contact.get_contact_list()

    app.contact.select_first_contact()
    app.contact.delete_contact()

    new_contacts = app.contact.get_contact_list()

    assert (len(old_contacts)-1) == len(new_contacts), "Количество контактов не соответствует"

    old_contacts.pop(0)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,
                                                                 key=Contact.id_or_max), "Отсортированные списки не совпадают"
