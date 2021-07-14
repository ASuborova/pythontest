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
        # select first element
        wd.find_element_by_name("selected[]").click()

    def create_group(self, group):
        wd = self.gr.wd
        # open page group
        self.open_group_page()
        # init new group
        wd.find_element_by_name("new").click()
        #
        self.attributes_group(group)
        # create new group
        wd.find_element_by_name("submit").click()
        # back page group
        self.back_page_group()

    def edit_first_group(self, group):
        wd = self.gr.wd
        # open page group
        self.open_group_page()
        self.select_first_element()
        # click edit group
        wd.find_element_by_name("edit").click()
        # get attributes group
        self.attributes_group(group)
        # update selected group
        wd.find_element_by_name("update").click()
        # back page group
        self.back_page_group()

    def del_first_group(self):
        wd = self.gr.wd
        # open page group
        self.open_group_page()
        self.select_first_element()
        # click and delete selected element
        wd.find_element_by_xpath("//input[@value='Delete group(s)']").click()
        # back page group
        self.back_page_group()

    def back_page_group(self):
        wd = self.gr.wd
        if wd.current_url.endswith("/group.php") and wd.find_element_by_link_text("group page").text == "group page":
            wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.gr.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.gr.wd
        self.open_group_page()
        group_list = []
        for element in (wd.find_elements_by_css_selector("span.group")):
            text_group = element.text
            id_group = element.find_element_by_name("selected[]").get_attribute("value")
            group_list.append(Group(id=id_group, namegroup=text_group))
        return list(group_list)
