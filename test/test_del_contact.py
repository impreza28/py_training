import allure
from model.contact import Contact

@allure.epic("Тесты удаления контактов")
@allure.description("Авторизация и удаление первого контакта")
def test_delete_contact(app):
    app.contact.open_contact_page()
    app.contact.select_first_contact()
    app.contact.delete_contact()
