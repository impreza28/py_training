from fixture.application import Application
import allure
import pytest

from model.group import Group
from sys import maxsize
import random
import string
from data.groups import testdata as data_groups



@allure.epic("Тесты добавления группы")
@allure.description("Авторизация и добавление новой группы (чтение из json_groups)")
def test_add_group_gen(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.open_group_page()
    app.group.create_group(group)
    new_groups = app.group.get_group_list()

    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,  key = Group.id_or_max)


@allure.description("Авторизация и добавление новой группы (БД)")
def test_add_group_with_db_check(app, json_groups, db,check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.open_group_page()
    app.group.create_group(group)
    new_groups = db.get_group_list()

    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,  key = Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



