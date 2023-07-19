import pymysql
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                contact_list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return contact_list

    def get_contact_list_full_info(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, lastname, firstname, address, email, email2, email3, home, mobile, work FROM addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, lastname, firstname, address, email, email2, email3, home, mobile, work) = row
                contact_list.append(Contact(id=str(id), lastname=lastname, firstname=firstname, address=address, email=email,
                                            email2=email2, email3=email3, homephone=home, mobilephone=mobile, workphone=work, all_emails_from_home_page=(email+email2+email3),
                                            all_phones_from_home_page=(home+mobile+work)))
        finally:
            cursor.close()
        return contact_list

    def get_contact_in_group_by_id(self, group_id, contact_id):
        group = []
        contacts = []
        list_contacts_in_group=[]
        cursor = self.connection.cursor()
        try:

            cursor.execute(f"SELECT id, group_id FROM address_in_groups where group_id='{group_id}' and id='{contact_id}'")
            for row in cursor:
                (id, group_id) = row
                list_contacts_in_group.append(id)
                list_contacts_in_group.append(group_id)

                #list_contacts_in_group.append(Group(id=str(group_id)))

        finally:
            cursor.close()
        return list_contacts_in_group


    def clean(self, group):
        return Group(id=group.id,name=group.name.strip())

    def destroy(self):
        self.connection.close()

