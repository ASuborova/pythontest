from model.contact import Contact
from model.group import Group
from model.contact import Contact
from model.contact_in_group import Contact_in_Group
import random


def test_add_contact_in_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.cont_h.create(Contact(lastname="test"))
    if len(db.get_group_list()) == 0:
        app.gr.create_group(Group(namegroup="test"))
    new_contact_in_group = Contact_in_Group(id="1", id_group="1")
    old_list_contact_in_group = db.get_contact_in_group_list()
    list_contact = db.get_contact_list()
    list_group = db.get_group_list()
    choice_id_contact = random.choice(list_contact)
    choice_id_group = random.choice(list_group)
    app.cont_gr.add_contact_in_group(choice_id_contact.id, choice_id_group.id)
    new_list_contact_in_group = db.get_contact_in_group_list()
    assert len(old_list_contact_in_group) + 1 == len(new_list_contact_in_group)
    old_list_contact_in_group.append(new_contact_in_group)
    assert old_list_contact_in_group == new_list_contact_in_group

    if check_ui:
        assert sorted(new_list_contact_in_group, key=Contact_in_Group.id_max) == sorted(app.cont_gr.get_list_contact_in_group(), key=Contact_in_Group.id_max)


