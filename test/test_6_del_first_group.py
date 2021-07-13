from model.group import Group


def test_del_first_group(app):
    if app.gr.count() == 0:
        app.gr.create_group(Group(namegroup="test"))
    old_groups = app.gr.get_group_list()
    app.gr.del_first_group()
    new_groups = app.gr.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


