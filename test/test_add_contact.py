import pytest
import allure
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@allure.epic("Тесты добавления контактов")
@allure.description("Авторизация и добавление нового контакта")
def test_add_contact(app):

    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Lara", middlename="Sergeevna", lastname="Kroft"))
    app.return_to_home_page()
