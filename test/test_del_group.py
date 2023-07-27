import random

import allure
from model.group import Group
from  random import randrange


@allure.epic("Тесты удаления групп")
@allure.description("Авторизация и удаление 1й группы")
def test_delete_first_group(app):
    app.group.open_group_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    if app.group.count_groups() == 0:
        app.group.create_group(Group(name="name группа", header="header группа", footer="footer группа"))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups), "Количество контактов не соответствует"
    old_groups.pop(index)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,
                                                                 key=Group.id_or_max), "Отсортированные списки не совпадают"


@allure.description("Авторизация и удаление группы (БД)")
def test_delete_group_with_db(app, db, check_ui):
    app.group.open_group_page()
    if app.group.count_groups() == 0:
        app.group.create_group(Group(name="name группа", header="header группа", footer="footer группа"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)

    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups), "Количество контактов не соответствует"
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,
                                                                 key=Group.id_or_max), "Отсортированные списки не совпадают"
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max), "Отсортированные списки не совпадают"

