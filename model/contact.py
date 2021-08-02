from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, companyname=None, address=None, homephone=None,
                 mobilephone=None, workphone=None, mainemail=None, email2=None, email3=None, bday="1", bmonth=None, byear=None, id=None,
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
        self.mainemail = mainemail
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        # self.bmonth = bmonth
        # self.byear = byear
        self.id = id
        self.emails_home = emails_home
        self.phones_home = phones_home
        self.emails_view = emails_view
        self.phones_view = phones_view
        self.aday = aday
        # self.amonth = amonth
        # self.ayear = ayear

    def __repr__(self):
        return "%s:%s %s %s %s %s %s %s %s %s" % (self.id, self.lastname, self.firstname, self.address,
                                                  self.mobilephone, self.homephone, self.workphone, self.mainemail,
                                                  self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id), \
               self.lastname is None or other.lastname is None or self.lastname == other.lastname, \
               self.firstname is None or other.firstname is None or self.firstname == other.firstname, \
               self.address is None or other.address is None or self.address == other.address, \
               self.emails_home is None or other.emails_home is None or self.emails_home == other.emails_home, \
               self.mainemail is None or other.mainemail is None or self.mainemail == other.mainemail, \
               self.email2 is None or other.email2 is None or self.email2 == other.email2, \
               self.email3 is None or other.email3 is None or self.email3 == other.email3, \
               self.phones_home is None or other.phones_home is None or self.phones_home == other.phones_home, \
               self.mobilephone is None or other.mobilephone is None or self.mobilephone == other.mobilephone, \
               self.homephone is None or other.homephone is None or self.homephone == other.homephone, \
               self.workphone is None or other.workphone is None or self.workphone == other.workphone

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
