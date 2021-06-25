from selenium import webdriver
from session.sessionhelper import SessionHelper
from session.contacthelper import ContactHelper


class Applicatin:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.ses_h = SessionHelper(self)
        self.cont_h = ContactHelper(self)

    def back_home_page(self):
        wd = self.wd
        # back home page
        wd.find_element_by_link_text("home page").click()

    def district(self):
        self.wd.quit()
