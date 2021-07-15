from model.group import Group


def test_add_group(app):
    old_groups = app.gr.get_group_list()
    group = Group(namegroup="group_1", header="Zagolovok", footer="Podval")
    app.gr.create_group(group)
    new_groups = app.gr.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
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



