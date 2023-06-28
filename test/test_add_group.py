
import allure
from model.group import Group
from sys import maxsize

@allure.epic("Тесты добавления группы")
@allure.description("Авторизация и добавление новой группы")
def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.open_group_page()
    group = Group(name="Группа1", header="header1", footer="footer2")
    app.group.create_group(group)
    new_groups = app.group.get_group_list()

    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,  key = Group.id_or_max)

@allure.description("Авторизация и добавление новой группы без данных")
def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.open_group_page()
    group = Group(name="", header="", footer="")
    app.group.create_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,  key = Group.id_or_max)

