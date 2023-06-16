import allure
from model.group import Group

@allure.epic("Тесты изменения группы")
@allure.description("Авторизация и изменение группы")
def test_modify_group(app):
    app.group.open_group_page()
    app.group.select_first_group()
    app.group.modify_group(Group(name="New name", header="New header", footer="New footer"))

@allure.description("Авторизация и изменение name группы")
def test_modify_group_name(app):
    app.group.open_group_page()
    app.group.select_first_group()
    app.group.modify_group(Group(name="New name"))