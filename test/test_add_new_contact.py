# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from fixture.application import Applicatin


@pytest.fixture
def app():
    fixture_create = Applicatin()
    yield fixture_create
    Applicatin.test_district(fixture_create)


def test_add_test_new_contact(app):
    app.ses_h.test_login(loginname="admin", password="secret")
    app.cont_h.test_create_new_contact(
        Contact(firstname="Anna", middlename="Maria", lastname="Suborova", nickname="ASuboroa", title="friends",
                companyname="signatec", address="Novosibirsk",
                homephone="+79232274031", mobilephone="3834156789",
                mainemail="a.suborov_a@gmail.com", email2="anna_suborova@mail.ru", bday="2",
                bmonth="November", byear="1979"))
    app.ses_h.test_logout()


def test_add_empty_test_new_contact(app):
    app.ses_h.test_login(loginname="admin", password="secret")
    app.cont_h.test_create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", companyname="",
                                       address="",
                                       homephone="", mobilephone="", mainemail="", email2="", bday="",
                                       bmonth="-", byear=""))
    app.ses_h.test_logout()
