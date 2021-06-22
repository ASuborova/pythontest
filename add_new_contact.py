# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Aplicatin


@pytest.fixture
def app_fix(fix_request):
    fixture_create = Aplicatin()
    fix_request.addfinalizer(fixture_create.district)
    return fixture_create


def add_test_new_contact(app_fix):
    app_fix.login(loginname="admin", password="secret")
    app_fix.create_new_contact(Contact(firstname="Anna", middlename="Maria", lastname="Suborova", nickname="ASuboroa", title="friends", companyname="signatec", address="Novosibirsk",
                                        homephone="+79232274031", mobilephone="3834156789",
                                        mainemail="a.suborov_a@gmail.com", email2="anna_suborova@mail.ru", bday="28",
                                        bmonth="November", byear="1984"))
    app_fix.logout()


def add_empty_test_new_contact(app_fix):
    app_fix.login("admin", "secret")
    app_fix.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", companyname="",
                                        address="",
                                        homephone="", mobilephone="", mainemail="", email2="", bday="",
                                        bmonth="-", byear=""))
    app_fix.logout()