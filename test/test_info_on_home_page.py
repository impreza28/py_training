import re
from random import randrange
from model.contact import Contact

def test_info_on_home_page(app):
    app.contact.open_contact_page()

    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]

    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page),\
        "all_phones не совпадают"
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname, \
        "firstname не совпадают"
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname, \
        "lastname не совпадают"
    assert contact_from_home_page.address == contact_from_edit_page.address, \
        "Адресы не совпадают"
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page), \
        "emails не совпадают"

def test_info_on_home_page_with_db(app, db):
    app.contact.open_contact_page()
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"))
        app.contact.return_to_home_page()

    contact_from_home_page = sorted(app.contact.get_contact_list(), key = Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list_full_info(), key = Contact.id_or_max)

    assert len(contact_from_home_page) == len(contact_from_db)

    assert contact_from_db == contact_from_home_page, "Список контактов из БД не совпадает со списком из UI"

















def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,
                                        contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))
