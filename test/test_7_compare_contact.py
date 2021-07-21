from model.contact import Contact
from random import randrange


def test_compare_some_contact(app):
    if app.cont_h.count() == 0:
        app.cont_h.create(Contact())
    old_list_contact = app.cont_h.get_list_contact()
    index_edit_contact = randrange(len(old_list_contact))
    contact = Contact(lastname="new lastname", firstname="New_firstname")
    contact.id = old_list_contact[index_edit_contact].id
    app.cont_h.compare_contact_by_index(contact, index_edit_contact)
    new_list_contact = app.cont_h.get_list_contact()
    assert len(old_list_contact) == len(new_list_contact)
    old_list_contact[index_edit_contact] = contact
    assert sorted(old_list_contact, key=Contact.id_max) == sorted(new_list_contact, key=Contact.id_max)