import allure
from model.contact import Contact

@allure.epic("Тесты удаления контактов")
@allure.description("Авторизация и удаление первого контакта")
def test_delete_contact(app):
    app.contact.open_contact_page()
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()
    app.contact.select_first_contact()
    app.contact.delete_contact()
