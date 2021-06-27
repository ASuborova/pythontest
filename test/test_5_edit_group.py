from model.group import Group


def test_edit_group(app):
    app.ses_h.login(loginname="admin", password="secret")
    app.gr.edit_first_group(Group(namegroup="...", header="...", footer="..."))
    app.ses_h.logout()
