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

    def get_list_contact_join(self):
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
                text_email_home = cells[4].text
                text_phone_home = cells[5].text
                self.contact_cash.append(
                    Contact(id=id_contact, lastname=text_lastname, firstname=text_firstname, address=text_address,
                            emails_home=text_email_home, phones_home=text_phone_home))
        return list(self.contact_cash)

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
                all_emails = cells[4].text.splitlines()
                all_phones = cells[5].text.splitlines()
                self.contact_cash.append(
                    Contact(id=id_contact, lastname=text_lastname, firstname=text_firstname, address=text_address,
                            mainemail=all_emails[0], email2=all_emails[1],
                            email3=all_emails[2], homephone=all_phones[0], mobilephone=all_phones[1],
                            workphone=all_phones[2]))
        return list(self.contact_cash)

    def open_contact_to_edit_by_index(self, index):
        wd = self.cont_h.wd
        self.cont_h.open_home_page()
        row = wd.find_elements_by_css_selector("[name=entry]")[index]
        cells = row.find_elements_by_tag_name("td")[7]
        cells.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.cont_h.wd
        self.cont_h.open_home_page()
        row = wd.find_elements_by_css_selector("[name=entry]")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_fio_view_by_index(self, index):
        wd = self.cont_h.wd
        self.cont_h.open_home_page()
        row = wd.find_elements_by_css_selector("[name=entry]")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("b").click()

    def join_get_contact_info_from_edit_page(self, index):
        wd = self.cont_h.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id_contact = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, middlename=middlename, mainemail=email, email2=email2, email3=email3,
                       id=id_contact, homephone=home, mobilephone=mobile, workphone=work, address=address)

    def join_get_contact_info_from_view_page(self, index):
        wd = self.cont_h.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        all_phones = ""

        if re.search("H: (.*)", text):
            homephone = ''.join(re.findall(r'[^H]', re.search("H: (.*)", text).group(1)))
            all_phones = homephone
        if re.search("M: (.*)", text) and all_phones != "":
            mobilephone = ''.join(re.findall(r'[^M]', re.search("M: (.*)", text).group(1)))
            all_phones = all_phones + '\n' + mobilephone
        elif re.search("M: (.*)", text) and all_phones == "":
            mobilephone = ''.join(re.findall(r'[^M]', re.search("M: (.*)", text).group(1)))
            all_phones = all_phones + mobilephone
        if re.search("W: (.*)", text) and all_phones != "":
            workphone = ''.join(re.findall(r'[^W]', re.search("W: (.*)", text).group(1)))
            all_phones = all_phones + '\n' + workphone
        elif re.search("W: (.*)", text) and all_phones == "":
            workphone = ''.join(re.findall(r'[^W]', re.search("W: (.*)", text).group(1)))
            all_phones = all_phones + workphone

        emails_list = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
        all_emails = '\n'.join(emails_list)

        return Contact(phones_view=all_phones, emails_view=all_emails)

    def join_get_contact_fio_info_from_view_page(self, index):
        wd = self.cont_h.wd
        self.open_contact_fio_view_by_index(index)
        fio = wd.find_element_by_id("content").text
        return Contact(fio_home=fio)




