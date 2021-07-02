# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.ses_h.login(loginname="admin", password="secret")
    app.cont_h.create(
        Contact(firstname="Anna_S", middlename="Maria", lastname="Suborova", nickname="A_Suborova", title="friends",
                companyname="signatec", address="Novosibirsk",
                homephone="+79232274031", mobilephone="3834156789",
                mainemail="a.suborov_a@gmail.com", email2="anna_suborova@mail.ru", bday="22", bmonth=None, byear="1988"))
    app.ses_h.logout()


'''def test_add_empty_contact(app):
    app.ses_h.login(loginname="admin", password="secret")
    app.cont_h.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", companyname="",
                                       address="", homephone="", mobilephone="", mainemail="", email2="", bday=None, bmonth=None, byear=None))
    app.ses_h.logout()'''

