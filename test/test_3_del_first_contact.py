from model.contact import Contact


def test_del_first_contact(app):
    if app.cont_h.count() == 0:
        app.cont_h.create(Contact(firstname="test", middlename=None, lastname=None, nickname=None, title=None, companyname=None,
                                  address=None, homephone=None, mobilephone=None, mainemail=None, email2=None, bday=None,
                                  bmonth=None, byear=None))
    app.cont_h.del_first_contact()

