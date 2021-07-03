
class SessionHelper:

    def __init__(self, ses_h):
        self.ses_h = ses_h

    def login(self, loginname, password):
        wd = self.ses_h.wd
        # open home page
        self.ses_h.open_home_page()
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(loginname)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_logout(self):
        wd = self.ses_h.wd
        if self.is_logged_in():
            self.logout()

    def logout(self):
        wd = self.ses_h.wd
        # logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def is_login(self, loginname, password):
        wd = self.ses_h.wd
        if self.is_logged_in():
            if self.is_logged_in_as(loginname):
                return
            else:
                self.logout()
        self.login(loginname, password)

    def is_logged_in(self):
        wd = self.ses_h.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, loginname):
        wd = self.ses_h.wd
        # return wd.find_element_by_xpath("div[@id='top']/form/b").text == "("+loginname+")"
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + loginname + ")"


