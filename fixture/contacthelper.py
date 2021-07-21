from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, cont_h):
        self.cont_h = cont_h

    def open_add_page(self):
        wd = self.cont_h.wd
        wd.find_element_by_link_text("add new").click()

    def select_first_element(self):
        wd = self.cont_h.wd
        wd.find_element_by_name("selected[]").click()

    def select_element_by_index(self, index_contact):
        wd = self.cont_h.wd
        wd.find_elements_by_name("selected[]")[index_contact].click()

    def attributes_contact(self, contact):
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
        self.change_field("work", contact.workphone)
        self.change_field("email", contact.mainemail)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
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
        self.cont_h.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.attributes_contact(contact)
        wd.find_element_by_name("submit").click()
        self.back_home_page()
        self.contact_cash = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index_element):
        wd = self.cont_h.wd
        self.cont_h.open_home_page()
        wd.find_elements_by_css_selector("img[alt='Edit']")[index_element].click()
        self.attributes_contact(contact)
        wd.find_element_by_name("update").click()
        self.back_home_page()
        self.contact_cash = None

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index_del_contact):
        wd = self.cont_h.wd
        self.cont_h.open_home_page()
        self.select_element_by_index(index_del_contact)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cash = None

    def back_home_page(self):
        wd = self.cont_h.wd
        if not(wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.cont_h.wd
        self.cont_h.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_list_contact(self):
        if self.contact_cash is None:
            wd = self.cont_h.wd
            self.cont_h.open_home_page()
            self.contact_cash = []
            for element in (wd.find_elements_by_css_selector("[name=entry]")):
                cells = element.find_elements_by_tag_name("td")
                id_contact = cells[0].find_element_by_tag_name("input").get_attribute("value")
                text_lastname = cells[1].text
                text_firstname = cells[2].text
                text_address = cells[3].text
                text_all_email = cells[4].text.splitlines()
                text_all_phone = cells[5].text.splitlines()
                self.contact_cash.append(
                    Contact(id=id_contact, lastname=text_lastname, firstname=text_firstname, address=text_address,
                            all_emails=text_all_email, all_phones=text_all_phone))

                # self.contact_cash.append(Contact(id=id_contact, lastname=text_lastname, firstname=text_firstname, address=text_address, mainemail=text_all_email[0], email2=text_all_email[1], email3=text_all_email[2], homephone=text_all_phone[0], mobilephone=text_all_phone[1], workphone=text_all_phone[2]))
        return list(self.contact_cash)

    def compare_contact_by_index(self, contact, index_compare_contact):
        wd = self.cont_h.wd
        self.cont_h.open_home_page()
        self.select_element_by_index(index_compare_contact)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cash = None

    def edit_contact_by_index(self, contact, index_element):
        wd = self.cont_h.wd
        self.cont_h.open_home_page()
        wd.find_elements_by_css_selector("img[alt='Edit']")[index_element].click()
        self.attributes_contact(contact)
        wd.find_element_by_name("update").click()
        self.back_home_page()
        self.contact_cash = None
