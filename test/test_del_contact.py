import allure
from model.contact import Contact

@allure.epic("Тесты удаления контактов")
@allure.description("Авторизация и удаление первого контакта")
def test_delete_contact(app):

    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
