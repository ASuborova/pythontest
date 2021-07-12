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
        return "%s:%s %s %s %s %s %s %s" % (self.id, self.lastname, self.firstname, self.address, self.mainemail, self.email2, self.homephone, self.mobilephone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and \
               (self.firstname is None or other.firstname is None or self.firstname == other.firstname) and \
               (self.address is None or other.address is None or self.address == other.address) and \
               (self.mainemail is None or other.mainemail is None or self.mainemail == other.mainemail) and \
               (self.email2 is None or other.email2 is None or self.email2 == other.email2) and \
               (self.homephone is None or other.homephone is None or self.homephone == other.homephone) and \
               (self.mobilephone is None or other.mobilephone is None or self.mobilephone == other.mobilephone)
