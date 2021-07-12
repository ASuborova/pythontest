from model.group import Group


def test_edit_name_group(app):
    if app.gr.count() == 0:
        app.gr.create_group(Group(namegroup="No_name", header="header_name", footer="footer_name"))
    old_groups = app.gr.get_group_list()
    app.gr.edit_first_group(Group(namegroup="New_group_name"))
    new_groups = app.gr.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_header_group(app):
    if app.gr.count() == 0:
        app.gr.create_group(Group(namegroup="New_name", header="", footer="footer_name"))
    old_groups = app.gr.get_group_list()
    app.gr.edit_first_group(Group(header="New header"))
    new_groups = app.gr.get_group_list()
    assert len(old_groups) == len(new_groups)
