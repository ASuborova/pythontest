class GroupHelper:

    def __init__(self, gr):
        self.gr = gr

    def open_group_page(self):
        wd = self.gr.wd
        # open page group
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.gr.wd
        # open page group
        self.open_group_page()
        # init new group
        wd.find_element_by_name("new").click()
        #
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.namegroup)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # create new group
        wd.find_element_by_name("submit").click()
        # back page group
        self.back_page_group()

    def edit_first_group(self, group):
        wd = self.gr.wd
        # open page group
        self.open_group_page()
        # select first element
        wd.find_element_by_name("selected[]").click()
        # edit select element
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.namegroup)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # edit selected group
        wd.find_element_by_name("update").click()
        # back page group
        self.back_page_group()

    def del_first_group(self):
        wd = self.gr.wd
        # open page group
        self.open_group_page()
        # select first element
        wd.find_element_by_name("selected[]").click()
        # click and delete selected element
        wd.find_element_by_xpath("//input[@value='Delete group(s)']").click()
        # back page group
        self.back_page_group()

    def back_page_group(self):
        wd = self.gr.wd
        # back page group
        wd.find_element_by_link_text("group page").click()
