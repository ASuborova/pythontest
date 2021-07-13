from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, companyname=None, address=None, homephone=None,
                           mobilephone=None, mainemail=None, email2=None, bday=None, bmonth=None, byear=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.companyname = companyname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.mainemail = mainemail
        self.email2 = email2
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
