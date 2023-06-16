import allure
from model.contact import Contact

@allure.epic("Тесты добавления контактов")
@allure.description("Авторизация и добавление нового контакта")
def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="Lara", middlename="Sergeevna", lastname="Kroft"))
    app.contact.return_to_home_page()

