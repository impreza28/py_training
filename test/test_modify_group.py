import allure
from model.group import Group
from random import randrange

@allure.epic("Тесты изменения группы")
@allure.description("Авторизация и изменение группы")
def test_modify_group(app):
    app.group.open_group_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    new_group = Group(name="name группа")
    new_group.id = old_groups[index].id
    if app.group.count_groups() == 0:
        app.group.create_group(new_group)
    app.group.select_group_by_index(index)
    app.group.modify_group(new_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = new_group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,  key = Group.id_or_max)

@allure.description("Авторизация и изменение name группы")
def test_modify_group_name(app):
    app.group.open_group_page()
    old_groups = app.group.get_group_list()
    if app.group.count_groups() == 0:
        app.group.create_group(Group(name="name группа",header="header группа",footer="footer группа"))
    app.group.select_first_group()
    app.group.modify_group(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



