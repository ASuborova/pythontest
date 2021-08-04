from model.contact import Contact
from random import randrange
import random


def test_edit_firstname_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.cont_h.create(Contact())
    old_list_contact = db.get_contact_list()
    index_edit_contact = random.choice(old_list_contact)
    contact = Contact(lastname="new lastname", firstname="New_firstname")
    contact.id = index_edit_contact.id
    app.cont_h.edit_contact_by_id(contact, index_edit_contact.id)
    new_list_contact = db.get_contact_list()
    assert len(old_list_contact) == len(new_list_contact)

    if check_ui:
        assert sorted(new_list_contact, key=Contact.id_max) == sorted(app.cont_h.get_list_contact(), key=Contact.id_max)

