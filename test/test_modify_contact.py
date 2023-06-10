import allure
from model.contact import Contact


@allure.epic("Тесты изменения контактов")
@allure.description("Авторизация и изменение первого контакта")
def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(firstname="New firstname", middlename="New middlename", lastname="New lastname"))
    app.session.logout()
