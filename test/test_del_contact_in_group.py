from model.group import Group
from model.contact import Contact
import random


def test_del_contact_in_group(app, db, DBORM):
    if len(db.get_contact_list()) == 0:
        app.cont_h.create(Contact(lastname="test_contact"))
    if len(db.get_group_list()) == 0:
        app.gr.create_group(Group(namegroup="test_group"))

    if len(db.get_contact_in_group_list()) == 0:
        list_group = db.get_group_list()
        choice_id_group = random.choice(list_group)
        contact_not_in_group = DBORM.get_contacts_not_in_group(choice_id_group)
        choice_id_contact = random.choice(contact_not_in_group)
        app.cont_gr.add_contact_in_group(choice_id_contact.id, choice_id_group)

    old_list_contact_in_group = DBORM.get_groups_with_contacts()

    choice_id_group = random.choice(old_list_contact_in_group)
    contact_in_group = DBORM.get_contacts_in_group(choice_id_group)

    choice_id_contact = random.choice(contact_in_group)

    app.cont_gr.del_contact_in_group_by_id(choice_id_contact.id, choice_id_group)

    new_list_contact_in_group = DBORM.get_contacts_in_group(choice_id_group)

    contact_in_group.remove(choice_id_contact)

    assert contact_in_group == new_list_contact_in_group



