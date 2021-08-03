import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
       self.host = host
       self.name = name
       self.user = user
       self.password = password
       self.connection = pymysql.connect(host=host,  database=name, user=user, password=password)
       self.connection.autocommit = True

    def get_group_list(self):
        list_group = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id_group, name, header, footer) = row
                list_group.append(Group(id=str(id_group), namegroup=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list_group

    def get_contact_list(self):
        list_contact = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated is Null")
            for row in cursor:
                (id_contact, firstname, lastname) = row
                list_contact.append(Contact(id=str(id_contact), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list_contact

    def district(self):
       self.connection.close()
