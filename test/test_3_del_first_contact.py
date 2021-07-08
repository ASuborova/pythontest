from model.contact import Contact


def test_del_first_contact(app):
    if app.cont_h.count() == 0:
        app.cont_h.create(Contact(firstname="test"))
    app.cont_h.del_first_contact()

