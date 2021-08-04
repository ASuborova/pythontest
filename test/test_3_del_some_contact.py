from model.contact import Contact
import random


def test_del_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.cont_h.create(Contact(lastname="test"))
    old_list_contact = db.get_contact_list()
    index_del_contact = random.choice(old_list_contact)
    app.cont_h.del_contact_by_id(index_del_contact.id)
    new_list_contact = db.get_contact_list()
    assert len(old_list_contact) - 1 == len(new_list_contact)
    old_list_contact.remove(index_del_contact)
    assert old_list_contact == new_list_contact

    if check_ui:
        assert sorted(new_list_contact, key=Contact.id_max) == sorted(app.cont_h.get_list_contact(), key=Contact.id_max)


