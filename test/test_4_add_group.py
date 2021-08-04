from model.group import Group


def test_add_group(app, json_groups, db, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.gr.create_group(group)
    new_groups = db.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_max) == sorted(new_groups, key=Group.id_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_max) == sorted(app.gr.get_group_list(), key=Group.id_max)





