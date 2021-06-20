# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

import group
from group import Group


class AddTestGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def logon(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def home_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_new_group(self, wd, group):
        # init group
        wd.find_element_by_name("new").click()
        #
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.namegroup)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.headergroup)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footergroup)
        # create new group
        wd.find_element_by_name("submit").click()

    def back_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_empty_test_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.logon(wd, username="admin", password="secret")
        self.home_group_page(wd)
        self.create_new_group(wd, group.Group(namegroup='', headergroup='', footergroup=''))
        self.back_to_group_page(wd)
        self.logout(wd)

    def add_test_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.logon(wd, username="admin", password="secret")
        self.home_group_page(wd)
        self.create_new_group(wd, group.Group(namegroup="new_group1", headergroup="new_group_1", footergroup="newgroup1"))
        self.back_to_group_page(wd)
        self.logout(wd)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
