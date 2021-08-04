# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app, json_contacts, db, check_ui):
    new_contact = json_contacts
    old_list_contact = db.get_contact_list()
    app.cont_h.create(new_contact)
    new_list_contact = db.get_contact_list()
    assert len(old_list_contact) + 1 == len(new_list_contact)
    old_list_contact.append(new_contact)
    assert sorted(old_list_contact, key=Contact.id_max) == sorted(new_list_contact, key=Contact.id_max)

    if check_ui:
        assert sorted(new_list_contact, key=Contact.id_max) == sorted(app.cont_h.get_list_contact(), key=Contact.id_max)



