from model.contact import Contact


def test_compare_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.cont_h.create(Contact(lastname="test"))

    ui_list = app.cont_h.get_list_contact()

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip())

    db_list = map(clean, db.get_contact_list())

    assert sorted(ui_list, key=Contact.id_max) == sorted(db_list, key=Contact.id_max)

