from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, cont_h):
        self.cont_h = cont_h

    def open_add_page(self):
        wd = self.cont_h.wd
        # open page add new contact
        wd.find_element_by_link_text("add new").click()

    def attributes_contact(self, contact):
        # get attributes contact
        wd = self.cont_h.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.companyname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.mainemail)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # wd.find_element_by_name("theform").click()

    def create(self, contact):
        wd = self.cont_h.wd
        # open page add new contact
        self.open_add_page()
        # get attributes contact
        self.attributes_contact(contact)
        # click create new contact
        wd.find_element_by_xpath("//input[@value='Enter']").click()
        # back nome page
        self.back_home_page()

    def edit_first_contact(self, contact):
        wd = self.cont_h.wd
        # open home page
        wd.find_element_by_link_text("home").click()
        # select edit contact
        wd.find_element_by_name("selected[]").click()
        # click edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # get attributes contact
        self.attributes_contact(contact)
        # click update
        wd.find_element_by_xpath("//input[@value='Update']").click()
        # back nome page
        self.back_home_page()

    def del_first_contact(self):
        wd = self.cont_h.wd
        # open home page
        wd.find_element_by_link_text("home").click()
        # select first element
        wd.find_element_by_name("selected[]").click()
        # click delete selected element
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # alert accept
        wd.switch_to_alert().accept()

    def back_home_page(self):
        wd = self.cont_h.wd
        # back home page
        wd.find_element_by_link_text("home page").click()
