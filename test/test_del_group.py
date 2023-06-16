import allure
from model.group import Group

@allure.epic("Тесты удаления групп")
@allure.description("Авторизация и удаление 1й группы")
def test_delete_first_group(app):
    app.group.open_group_page()
    if app.group.count_groups() == 0:
        app.group.create_group(Group(name="name группа",header="header группа",footer="footer группа"))
    app.group.delete_first_group()


