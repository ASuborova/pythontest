# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits # + string.punctuation + " "*3
    address_email = ["@gmail.com", "@mail.ru", "@ya.ru"]
    number = string.digits
    if prefix == 'email':
        return ("".join(random.choice(symbol) for i in range(random.randrange(maxlen)))
                + random.choice(address_email))
    elif prefix == 'number':
        return "".join(random.choice(number) for i in range(maxlen))
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


testdata = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), companyname=random_string("companyname", 10),
            address=random_string("address", 50), homephone=random_string("number", 11),
            mobilephone=random_string("number", 11), workphone=random_string("number", 11),
            mainemail=random_string("email", 5), email2=random_string("email", 5),
            email3=random_string("email", 5))
            for i in range(5)
            ]


@pytest.mark.parametrize("contact", testdata, ids=(repr(x) for x in testdata))
def test_add_new_contact(app, contact):
    new_contact = contact
    old_list_contact = app.cont_h.get_list_contact()
    app.cont_h.create(new_contact)
    assert len(old_list_contact) + 1 == app.cont_h.count()
    new_list_contact = app.cont_h.get_list_contact()
    old_list_contact.append(new_contact)
    assert sorted(old_list_contact, key=Contact.id_max) == sorted(new_list_contact, key=Contact.id_max)


