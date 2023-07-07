
import allure
import pytest

from model.group import Group
from sys import maxsize
import random
import string
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Group(name=name, header=header, footer=footer)
            for name in ["", random_string("name", 10)]
            for header in ["", random_string("header", 10)]
            for footer in ["", random_string("footer", 10)]]

@allure.epic("Тесты добавления группы")
@allure.description("Авторизация и добавление новой группы")
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):

    old_groups = app.group.get_group_list()
    app.group.open_group_page()
    app.group.create_group(group)
    new_groups = app.group.get_group_list()

    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,  key = Group.id_or_max)

