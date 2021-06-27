
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

    def logout(self):
        wd = self.ses_h.wd
        # logout
        wd.find_element_by_link_text("Logout").click()
        # wd.find_element_by_xpath("//input[@value='yes']").click()
