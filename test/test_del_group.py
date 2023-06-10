import allure

@allure.epic("Тесты удаления групп")
@allure.description("Авторизация и удаление 1й группы")
def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.delete_first_group()
    app.session.logout()


