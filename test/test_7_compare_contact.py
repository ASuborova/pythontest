from model.contact import Contact
from random import randrange
import re


def test_compare_contact(app):
    if app.cont_h.count() == 0:
        app.cont_h.create(Contact())
    all_contact = app.cont_h.get_list_contact()
    index_compare = randrange(len(all_contact))
    contact_from_view_page = app.cont_h.join_get_contact_info_from_view_page(index_compare)
    contact_from_edit_page = app.cont_h.join_get_contact_info_from_edit_page(index_compare)

    assert all_phones_on_view_page(contact_from_view_page) == all_phones_on_home_page(contact_from_edit_page)
    assert contact_from_view_page.emails_view == all_emails_on_home_page(contact_from_edit_page)


def all_phones_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clean(x), filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone]))))


def all_phones_on_view_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clean(x), filter(lambda x: x is not None, [contact.phones_view]))))


def all_emails_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clean(x), filter(lambda x: x is not None, [contact.mainemail, contact.email2, contact.email3]))))


def clean(s):
    return re.sub("[() -]", "", s)