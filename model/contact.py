from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, companyname=None, address=None, homephone=None,
                 mobilephone=None, workphone=None, mainemail=None, phone2=None, email2=None, email3=None, bday="1", bmonth=None, byear=None, id=None,
                 emails_home=None, phones_home=None, emails_view=None, phones_view=None, aday="1", amonth=None, ayear=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.companyname = companyname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.phone2 = phone2
        self.mainemail = mainemail
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.emails_home = emails_home
        self.phones_home = phones_home
        self.emails_view = emails_view
        self.phones_view = phones_view
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear

    def __repr__(self):
        return "%s:%s %s %s %s %s %s %s %s %s %s" % (self.id, self.lastname, self.firstname, self.address,
                                                  self.mobilephone, self.homephone, self.workphone, self.phone2, self.mainemail,
                                                  self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname \
               and self.firstname == other.firstname

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
