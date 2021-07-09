from model.group import Group


def test_add_group(app):
    old_groups = app.gr.get_group_list()
    app.gr.create_group(Group(namegroup="group_1", header="Zagolovok", footer="Podval"))
    new_groups = app.gr.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.gr.get_group_list()
    app.gr.create_group(Group())
    new_groups = app.gr.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)



