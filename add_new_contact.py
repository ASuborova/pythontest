# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application import Applicatin

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.app = Applicatin()

    def add_test_new_contact(self):
        self.app.login("admin", "secret")
        self.app.create_new_contact(Contact(firstname="Anna", middlename="Maria", lastname="Suborova", nickname="ASuboroa",
                                        title="friends", companyname="signatec", address="Novosibirsk",
                                        homephone="+79232274031", mobilephone="3834156789",
                                        mainemail="a.suborov_a@gmail.com", email2="anna_suborova@mail.ru", bday="28",
                                        bmonth="November", byear="1984"))
        self.app.logout()

    def add_empty_test_new_contact(self):
        self.app.login("admin", "secret")
        self.app.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", companyname="",
                                        address="",
                                        homephone="", mobilephone="", mainemail="", email2="", bday="",
                                        bmonth="-", byear=""))
        self.app.logout()

    def tearDown(self):
        self.app.district()

if __name__ == "__main__":
    unittest.main()
