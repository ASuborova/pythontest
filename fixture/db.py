import pymysql.cursors
from model.group import Group
from model.contact import Contact
from model.contact_in_group import Contact_in_Group


class DbFixture:

    def __init__(self, host, name, user, password):
       self.host = host
       self.name = name
       self.user = user
       self.password = password
       self.connection = pymysql.connect(host=host,  database=name, user=user, password=password, autocommit=True)

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
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 "
                           "from addressbook where deprecated is Null")
            for row in cursor:
                (id_contact, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list_contact.append(Contact(id=str(id_contact), firstname=firstname, lastname=lastname,
                                            address=address, homephone=home, mobilephone=mobile, workphone=work,
                                            phone2=phone2, mainemail=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list_contact

    def get_contact_in_group_list(self):
        list_contact = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated is Null")
            for row in cursor:
                (id_contact, id_group) = row
                list_contact.append(Contact_in_Group(id=str(id_contact), group_id=str(id_group)))
        finally:
            cursor.close()
        return list_contact

    def district(self):
       self.connection.close()
