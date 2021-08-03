from model.group import Group


def test_add_group(app, db, json_groups):
    group = json_groups
    # old_groups = app.gr.get_group_list()
    old_groups = db.get_group_list()
    app.gr.create_group(group)
    # assert len(old_groups) + 1 == app.gr.count()
    # new_groups = app.gr.get_group_list()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_max) == sorted(new_groups, key=Group.id_max)




