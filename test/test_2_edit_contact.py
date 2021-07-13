from model.contact import Contact


def test_edit_firstname_contact(app):
    if app.cont_h.count() == 0:
        app.cont_h.create(Contact())
    old_list_contact = app.cont_h.get_list_contact()
    contact = Contact(firstname="New_firstname")
    contact.id = old_list_contact[0].id
    app.cont_h.edit_first_contact(contact)
    new_list_contact = app.cont_h.get_list_contact()
    assert len(old_list_contact) == len(new_list_contact)
    old_list_contact[0] = contact
    assert sorted(old_list_contact, key=Contact.id_max) == sorted(new_list_contact, key=Contact.id_max)
