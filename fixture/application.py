from selenium import webdriver
from fixture.sessionhelper import SessionHelper
from fixture.contacthelper import ContactHelper
from fixture.grouphelper import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.ses_h = SessionHelper(self)
        self.cont_h = ContactHelper(self)
        self.gr = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # home page
        wd.get("http://localhost/addressbook/index.php")

    def district(self):
        self.wd.quit()
