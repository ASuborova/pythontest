from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, cont_h):
        self.cont_h = cont_h

    def open_add_page(self):
        wd = self.cont_h.wd
        # open page add new contact
        wd.find_element_by_link_text("add new").click()

    def select_first_element(self):
        wd = self.cont_h.wd
        # select first element
        wd.find_element_by_name("selected[]").click()

    def attributes_contact(self, contact):
        # get attributes contact
        wd = self.cont_h.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("title", contact.title)
        self.change_field("company", contact.companyname)
        self.change_field("address", contact.address)
        self.change_field("home", contact.homephone)
        self.change_field("mobile", contact.mobilephone)
        self.change_field("email", contact.mainemail)
        self.change_field("email2", contact.email2)
        self.change_field("bday", contact.bday)
        self.change_field("bmonth", contact.bmonth)
        self.change_field("byear", contact.byear)

    def change_field(self, field_name, text):
        wd = self.cont_h.wd
        if text is not None:
            if (field_name == "bday") or (field_name == "bmonth"):
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

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
        self.select_first_element()
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
        self.select_first_element()
        # click delete selected element
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # alert accept
        wd.switch_to_alert().accept()

    def back_home_page(self):
        wd = self.cont_h.wd
        # back home page
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.cont_h.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))
