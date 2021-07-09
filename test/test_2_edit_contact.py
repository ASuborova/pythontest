from model.contact import Contact


def test_edit_firstname_contact(app):
    if app.cont_h.count() == 0:
        app.cont_h.create(Contact(firstname=""))
    old_list_contact = app.cont_h.get_list_contact()
    app.cont_h.edit_first_contact(Contact(firstname="New_name", lastname="New_name"))
    new_list_contact = app.cont_h.get_list_contact()
    assert len(old_list_contact) == len(new_list_contact)

