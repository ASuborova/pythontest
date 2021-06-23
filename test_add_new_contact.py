# -*- coding: utf-8 -*-
import pytest

from contact import Contact
from application import Applicatin


@pytest.fixture
def app():
    fixture_create = Applicatin()
    yield fixture_create
    Applicatin.test_district(fixture_create)


def test_add_test_new_contact(app):
    app.test_login(loginname="admin", password="secret")
    app.test_create_new_contact(
        Contact(firstname="Anna", middlename="Maria", lastname="Suborova", nickname="ASuboroa", title="friends",
                companyname="signatec", address="Novosibirsk",
                homephone="+79232274031", mobilephone="3834156789",
                mainemail="a.suborov_a@gmail.com", email2="anna_suborova@mail.ru", bday="28",
                bmonth="November", byear="1984"))
    app.test_logout()


def test_add_empty_test_new_contact(app):
    app.test_login("admin", "secret")
    app.test_create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", companyname="",
                                       address="",
                                       homephone="", mobilephone="", mainemail="", email2="", bday="",
                                       bmonth="-", byear=""))
    app.test_logout()
