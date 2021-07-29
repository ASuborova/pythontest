from model.group import Group
import random
import string

constant = [
    Group(namegroup="name1", header="header1", footer="footer1"),
    Group(namegroup="name2", header="header2", footer="footer2")
]


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


testdata = [Group(namegroup="", header="", footer="")] + [
    Group(namegroup=random_string("group_name", 2), header=random_string("Zagolovok", 5), footer=random_string("Podval", 5))
    for i in range(5)
]
