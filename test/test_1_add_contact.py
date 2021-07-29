# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app, json_contacts):
    new_contact = json_contacts
    old_list_contact = app.cont_h.get_list_contact()
    app.cont_h.create(new_contact)
    assert len(old_list_contact) + 1 == app.cont_h.count()
    new_list_contact = app.cont_h.get_list_contact()
    old_list_contact.append(new_contact)
    assert sorted(old_list_contact, key=Contact.id_max) == sorted(new_list_contact, key=Contact.id_max)


