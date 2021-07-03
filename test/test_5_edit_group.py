from model.group import Group


def test_edit_name_group(app):
    app.gr.edit_first_group(Group(namegroup="New_group_name", header=None, footer=None))



'''def test_edit_header_group(app):
    app.gr.edit_first_group(Group(namegroup=None, header="New header", footer=None))
    app.ses_h.logout()'''
