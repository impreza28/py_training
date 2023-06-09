import pytest
import allure
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@allure.epic("Тесты добавления группы")
@allure.description("Авторизация и добавление новой группы")
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(Group(name="Группа1", header="header1", footer="footer2"))
    app.session.logout()

@allure.description("Авторизация и добавление новой группы без данных")
def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()


