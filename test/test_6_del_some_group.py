from model.group import Group
from random import randrange


def test_del_some_group(app):
    if app.gr.count() == 0:
        app.gr.create_group(Group(namegroup="test"))
    old_groups = app.gr.get_group_list()
    index_del_group = randrange(len(old_groups))
    app.gr.del_group_by_index(index_del_group)
    new_groups = app.gr.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index_del_group:index_del_group+1] = []
    assert old_groups == new_groups


