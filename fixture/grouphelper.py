from model.group import Group

class GroupHelper:

    def __init__(self, gr):
        self.gr = gr

    def open_group_page(self):
        wd = self.gr.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def attributes_group(self, group):
        wd = self.gr.wd
        self.change_field("group_name", group.namegroup)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.gr.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_element(self):
        wd = self.gr.wd
        wd.find_element_by_name("selected[]").click()

    def select_element_by_index(self, index_element):
        wd = self.gr.wd
        wd.find_elements_by_name("selected[]")[index_element].click()

    def select_element_by_id(self, id_group):
        wd = self.gr.wd
        wd.find_element_by_css_selector("input[value='%s']" % id_group).click()

    def create_group(self, group):
        wd = self.gr.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.attributes_group(group)
        wd.find_element_by_name("submit").click()
        self.back_page_group()
        self.group_cash = None

    def edit_first_group(self, group):
        self.edit_group_by_index(group, 0)

    def edit_group_by_index(self, group, index_group):
        wd = self.gr.wd
        self.open_group_page()
        self.select_element_by_index(index_group)
        wd.find_element_by_name("edit").click()
        self.attributes_group(group)
        wd.find_element_by_name("update").click()
        self.back_page_group()
        self.group_cash = None

    def edit_group_by_id(self, group, id_group):
        wd = self.gr.wd
        self.open_group_page()
        self.select_element_by_id(id_group)
        wd.find_element_by_name("edit").click()
        self.attributes_group(group)
        wd.find_element_by_name("update").click()
        self.back_page_group()
        self.group_cash = None

    def del_first_group(self):
        self.del_group_by_index(0)

    def back_page_group(self):
        wd = self.gr.wd
        if wd.current_url.endswith("/group.php") and wd.find_element_by_link_text("group page").text == "group page":
            wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.gr.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cash = None

    def get_group_list(self):
        if self.group_cash is None:
            wd = self.gr.wd
            self.open_group_page()
            self.group_cash = []
            for element in (wd.find_elements_by_css_selector("span.group")):
                text_group = element.text
                id_group = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cash.append(Group(id=id_group, namegroup=text_group))
        return list(self.group_cash)

    def del_group_by_index(self, index_dy_group):
        wd = self.gr.wd
        self.open_group_page()
        self.select_element_by_index(index_dy_group)
        wd.find_element_by_name("delete").click()
        self.back_page_group()
        self.group_cash = None

    def del_group_by_id(self, id_group):
        wd = self.gr.wd
        self.open_group_page()
        self.select_element_by_id(id_group)
        wd.find_element_by_name("delete").click()
        self.back_page_group()
        self.group_cash = None



