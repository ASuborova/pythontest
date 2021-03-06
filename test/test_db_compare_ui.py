from model.group import Group


def test_group_list(app, db):
    ui_list = app.gr.get_group_list()

    def clean(group):
        return Group(id=group.id, namegroup=group.namegroup.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_max) == sorted(db_list, key=Group.id_max)
