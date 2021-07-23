from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*3
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


testdata = [Group(namegroup="", header="", footer="")] + [
    Group(namegroup=random_string("group_name", 2), header=random_string("Zagolovok", 5), footer=random_string("Podval", 5))
    for i in range(5)
]

# testdata = [
#    Group(namegroup=group_name, header=Zagolovok, footer=Podval)
#    for group_name in ["", random_string("group_name", 10)]
#    for Zagolovok in ["", random_string("Zagolovok", 20)]
#    for Podval in ["", random_string("Podval", 20)]
#]


@pytest.mark.parametrize("group", testdata, ids=(repr(x) for x in testdata))
def test_add_group(app, group):
    old_groups = app.gr.get_group_list()
    app.gr.create_group(group)
    assert len(old_groups) + 1 == app.gr.count()
    new_groups = app.gr.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_max) == sorted(new_groups, key=Group.id_max)


# def test_add_empty_group(app):
#    old_groups = app.gr.get_group_list()
#    group = Group(namegroup="", header="", footer="")
#    app.gr.create_group(group)
#    new_groups = app.gr.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_max) == sorted(new_groups, key=Group.id_max)



