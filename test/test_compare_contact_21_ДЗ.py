from model.contact import Contact
from random import randrange
import re


def test_compare_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.cont_h.create(Contact(lastname="test"))

    all_contact_from_home = sorted(app.cont_h.get_list_contact(), key=Contact.id_max)

    def clean_contact(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip(), mainemail=contact.mainemail.strip(),
                       email2=contact.email2.strip(), email3=contact.email3.strip(),
                       homephone=contact.homephone.strip(), workphone=contact.workphone.strip(),
                       mobilephone=contact.mobilephone.strip(), phone2=contact.phone2.strip())
    all_contact_from_db = sorted(list(map(clean_contact, db.get_contact_list())), key=Contact.id_max)

    assert len(all_contact_from_home) == len(all_contact_from_db)

    index_compare = range(len(all_contact_from_home))

    for i in index_compare:

        assert all_contact_from_home[i].id == all_contact_from_db[i].id
        assert all_contact_from_home[i].firstname == all_contact_from_db[i].firstname
        assert all_contact_from_home[i].lastname == all_contact_from_db[i].lastname
        assert all_contact_from_home[i].address == all_contact_from_db[i].address

        assert all_contact_from_home[i].emails_home == all_emails_on_home_page(all_contact_from_db[i])
        assert all_contact_from_home[i].phones_home == all_phones_on_home_page(all_contact_from_db[i])


def all_phones_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clean(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))


def all_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.mainemail, contact.email2, contact.email3]))


def clean(s):
    return re.sub("[() -]", "", s)
