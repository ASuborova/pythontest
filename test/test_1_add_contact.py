# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_list_contact = app.cont_h.get_list_contact()
    app.cont_h.create(
        Contact(firstname="Anna_S", middlename="Maria", lastname="Suborova", nickname="A_Suborova", title="friends",
                companyname="signatec", address="Novosibirsk",
                homephone="+79232274031", mobilephone="3834156789",
                mainemail="a.suborov_a@gmail.com", email2="anna_suborova@mail.ru", bday="22", byear="1988"))
    new_list_contact = app.cont_h.get_list_contact()
    assert len(old_list_contact) + 1 == len(new_list_contact)


def test_add_empty_contact(app):
    old_list_contact = app.cont_h.get_list_contact()
    app.cont_h.create(Contact())
    new_list_contact = app.cont_h.get_list_contact()
    assert len(old_list_contact) + 1 == len(new_list_contact)

