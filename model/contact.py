from sys import maxsize


class Contact:
    def __init__(self, firstname, lastname, middlename=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
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
