from selenium import webdriver
from fixture.sessionhelper import SessionHelper
from fixture.contacthelper import ContactHelper


class Applicatin:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.ses_h = SessionHelper(self)
        self.cont_h = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        # home page
        wd.get("http://localhost/addressbook/index.php")

    def district(self):
        self.wd.quit()
