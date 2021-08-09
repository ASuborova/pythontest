from selenium import webdriver
from fixture.sessionhelper import SessionHelper
from fixture.contacthelper import ContactHelper
from fixture.grouphelper import GroupHelper
from fixture.contact_in_group_helper import Contact_in_Group_Helper


class Application:
    def __init__(self, browser, BUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unknown browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.ses_h = SessionHelper(self)
        self.cont_h = ContactHelper(self)
        self.cont_gr = Contact_in_Group_Helper(self)
        self.gr = GroupHelper(self)
        self.BUrl = BUrl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # home page
        wd.get(self.BUrl)

    def district(self):
        self.wd.quit()
