import random
import time

from model.group import Group

class Contact_in_Group_Helper:

    def __init__(self, cont_gr):
        self.cont_gr = cont_gr

    def back_home_page(self):
        wd = self.cont_gr.wd
        if not(wd.current_url.endswith("addressbook/") and len(wd.find_element_by_name("to_group")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.cont_gr.wd
        self.cont_gr.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def del_contact_in_group_by_id(self, group, orm):
        wd = self.cont_gr.wd
        self.cont_gr.open_home_page()
        self.get_list_contact_in_group(group)
        if not wd.find_element_by_xpath("//div[@id='content]/label/strong/span[@id='search_count']").text == 0:
            contact_list_in_group = orm.get_contacts_in_group(Group(id='%s' % group))
            id_contact_del_in_group = random.randint(0, len(contact_list_in_group)-1)
            contact_del_in_group = contact_list_in_group[id_contact_del_in_group].id
            self.select_contact(contact_del_in_group)
            wd.find_element_by_name("remove").click()
            try:
                wd.find_element_by_xpath("//*[text() = 'Users removed.']")
            except Exception:
                time.sleep(0.1)

    def get_list_contact_in_group(self, group_id):
        wd = self.cont_gr.wd
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()

    def select_contact(self, id_contact):
        wd = self.cont_gr.wd
        # wd.find_element_by_css_selector("input[value='%s']" % id_contact).click()
        wd.find_element_by_id("%s" % id_contact).click()

    def select_group(self, id_group):
        wd = self.cont_gr.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[4]/select/option[%s]" % id_group).click()

    def add_contact_in_group(self, id_contact, id_group):
        wd = self.cont_gr.wd
        self.cont_gr.open_home_page()
        self.select_contact(id_contact)
        self.select_group(id_group)
        wd.find_element_by_name("add").click()
        try:
            wd.find_element_by_xpath("//*[text() = 'Users added']")
        except Exception:
            time.sleep(0.1)





