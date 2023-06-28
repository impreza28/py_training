import allure
from model.group import Group


@allure.epic("Тесты удаления групп")
@allure.description("Авторизация и удаление 1й группы")
def test_delete_first_group(app):
    app.group.open_group_page()
    old_groups = app.group.get_group_list()
    if app.group.count_groups() == 0:
        app.group.create_group(Group(name="name группа", header="header группа", footer="footer группа"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups), "Количество контактов не соответствует"
    old_groups.pop(0)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,
                                                                 key=Group.id_or_max), "Отсортированные списки не совпадают"
