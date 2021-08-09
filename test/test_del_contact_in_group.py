from model.contact import Contact
from model.group import Group
from model.contact_in_group import Contact_in_Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1",  name="addressbook", user="addressbook2", password="addressbook2")


def test_del_contact_in_group(app, db):
    global orm

    if len(db.get_contact_list()) == 0:
        app.cont_h.create(Contact(lastname="test"))
    if len(db.get_group_list()) == 0:
        app.gr.create_group(Group(namegroup="test"))

    list_group = db.get_group_list()
    random_group_number = random.randint(0, len(list_group))
    random_group_id = list_group[random_group_number].id

    old_list_contact_in_group = len(orm.get_contacts_in_group(Group(id='%s' % random_group_id)))

    if old_list_contact_in_group == 0:
        list_contact = db.get_contact_list()
        random_contact_number = random.choice(len(list_contact))
        app.cont_gr.add_contact_in_group(random_contact_number.id, random_group_number)

        app.cont_gr.del_contact_in_group_by_id(group=random_group_id, orm=orm)


    # index_del_contact_in_group = old_list_contact_in_group[random_number_group].group_id
    # app.cont_gr.del_contact_in_group_by_id(group=random_group_id, orm=orm)
    # new_list_contact_in_group = db.get_contact_in_group_list()

        new_list_contact_in_group = len(orm.get_contacts_in_group(Group(id='%s' % random_group_id)))

        assert len(old_list_contact_in_group) - 1 == len(new_list_contact_in_group)



