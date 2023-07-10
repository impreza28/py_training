
import allure
import pytest

from model.group import Group
from sys import maxsize
import random
import string
from data.groups import testdata as data_groups





#@allure.epic("Тесты добавления группы")
#@allure.description("Авторизация и добавление новой группы")
#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
#def test_add_group(app, group):
#
#    old_groups = app.group.get_group_list()
#    app.group.open_group_page()
#    app.group.create_group(group)
#    new_groups = app.group.get_group_list()
#
#    assert len(old_groups)+1 == len(new_groups)
#
#    old_groups.append(group)
#    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,  key = Group.id_or_max)


@allure.epic("Тесты добавления группы")
@allure.description("Авторизация и добавление новой группы")
def test_add_group_gen(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.open_group_page()
    app.group.create_group(group)
    new_groups = app.group.get_group_list()

    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,  key = Group.id_or_max)

