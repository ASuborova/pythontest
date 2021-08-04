from model.group import Group
from random import randrange
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.gr.create_group(Group())
    old_groups = db.get_group_list()
    index_edit_group = random.choice(old_groups)
    group = Group(namegroup="New_group_name")
    group.id = index_edit_group.id
    app.gr.edit_group_by_id(group, index_edit_group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)

    if check_ui:
        assert sorted(new_groups, key=Group.id_max) == sorted(app.gr.get_group_list(), key=Group.id_max)


