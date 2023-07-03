from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, middlename=None, id=None, homephone= None, mobilephone = None, workphone = None, secondaryphone = None,
                 all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page= all_phones_from_home_page

        #self.contact_row = contact_row

    def __eq__(self, other):
        return (
                    self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname \
            and (self.middlename is None or other.middlename is None or self.middlename == other.middlename)

    def __repr__(self):
        return "%s; %s; %s" % (self.id, self.lastname, self.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
