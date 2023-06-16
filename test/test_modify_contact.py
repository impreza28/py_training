import allure
from model.contact import Contact


@allure.epic("Тесты изменения контактов")
@allure.description("Авторизация и изменение первого контакта")
def test_modify_contact(app):
    app.contact.open_contact_page()
    app.contact.select_first_contact()
    app.contact.modify_contact(
        Contact(firstname="New firstname", middlename="New middlename", lastname="New lastname"))
 