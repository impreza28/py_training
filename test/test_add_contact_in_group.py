from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group_with_db(app, db):
    app.contact.open_contact_page()

    if db.get_contact_count() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()

    if db.get_group_count() == 0:
        app.group.open_group_page()
        app.group.create_group(Group(name="name группа", header="header группа", footer="footer группа"))

    # очистить таблицу address_in_groups от данных
    db.clear_table_address_in_groups()
    # выбрать контакт
    selected_contact = random.choice(app.contact.get_contact_list())
    # выбрать группу
    selected_group = random.choice(db.get_group_list())
    # добавить контакт в группу
    app.contact.add_contact_in_group(selected_contact.id, selected_group.id)
    # получить из бд группу с добавленной группой
    contact_in_group = db.get_contact_in_group_by_id(selected_group.id, selected_contact.id)

    assert str(contact_in_group[0]) == selected_contact.id and str(
        contact_in_group[1]) == selected_group.id, "Контакт не добавлен в группу"



