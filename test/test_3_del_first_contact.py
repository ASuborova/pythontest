from model.contact import Contact


def test_del_first_contact(app):
    if app.cont_h.count() == 0:
        app.cont_h.create(Contact(firstname="test"))
    old_list_contact = app.cont_h.get_list_contact()
    app.cont_h.del_first_contact()
    new_list_contact = app.cont_h.get_list_contact()
    assert len(old_list_contact) - 1 == len(new_list_contact)
    old_list_contact[0:1] = []
    assert old_list_contact == new_list_contact



