import random

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

@allure.description("Авторизация и изменение группы (с БД)")
def test_modify_group_with_db_check(app,db, check_ui):
    app.group.open_group_page()
    new_group = Group(name="name группа")
    if app.group.count_groups() == 0:
        app.group.create_group(new_group)

    old_groups = db.get_group_list()

    selected_group = random.choice(old_groups)
    app.group.select_group_by_id(selected_group.id)
    app.group.modify_group(new_group)
    new_groups = db.get_group_list()

    for i in range(len(old_groups)):
        for j in range(1):
            if old_groups[i].id == selected_group.id:
                old_groups[i].name = new_group.name
                break

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


