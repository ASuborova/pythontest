from selenium.webdriver.support.ui import Select
from model.contact import Contact



class ContactHelper:

    def __init__(self, cont_h):
        self.cont_h = cont_h

    def open_add_page(self):
        wd = self.cont_h.wd
        # open page add new contact
        wd.find_element_by_link_text("add new").click()

    def select_first_element(self):
        wd = self.cont_h.wd
        wd.find_element_by_name("selected[]").click()

    def select_element_by_index(self, index_contact):
        wd = self.cont_h.wd
        wd.find_elements_by_name("selected[]")[index_contact].click()

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
        self.contact_cash = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index_element):
        wd = self.cont_h.wd
        self.open_home_page()
        # self.select_first_element()
        self.select_element_by_index(index_element)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.attributes_contact(contact)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.back_home_page()
        self.contact_cash = None

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index_del_contact):
        wd = self.cont_h.wd
        self.open_home_page()
        # self.select_first_element()
        self.select_element_by_index(index_del_contact)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cash = None

    def open_home_page(self):
        wd = self.cont_h.wd
        if not(wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def back_home_page(self):
        wd = self.cont_h.wd
        if not(wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.cont_h.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_list_contact(self):
        if self.contact_cash is None:
            wd = self.cont_h.wd
            self.open_home_page()
            self.contact_cash = []
            for element in (wd.find_elements_by_css_selector("[name=entry]")):
                cells = element.find_elements_by_tag_name("td")
                id_contact = cells[0].find_element_by_name("selected[]").get_attribute("value")
                text_lastname = cells[1].text
                text_firstname = cells[2].text
                self.contact_cash.append(Contact(id=id_contact, lastname=text_lastname, firstname=text_firstname))
        return list(self.contact_cash)

