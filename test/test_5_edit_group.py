from model.group import Group


def test_edit_name_group(app):
    if app.gr.count() == 0:
        app.gr.create_group(Group())
    old_groups = app.gr.get_group_list()
    group = Group(namegroup="New_group_name")
    group.id = old_groups[0].id
    app.gr.edit_first_group(group)
    new_groups = app.gr.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_max) == sorted(new_groups, key=Group.id_max)


def test_edit_header_group(app):
    if app.gr.count() == 0:
        app.gr.create_group(Group())
    old_groups = app.gr.get_group_list()
    group = Group(header="New header")
    group.id = old_groups[0].id
    app.gr.edit_first_group(group)
    new_groups = app.gr.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_max) == sorted(new_groups, key=Group.id_max)

