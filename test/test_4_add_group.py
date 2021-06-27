from model.group import Group


def test_add_group(app):
    app.ses_h.login(loginname="admin", password="secret")
    app.gr.create_group(Group(namegroup="group_1", header="Zagolovok", footer="Podval"))
    app.ses_h.logout()


def test_add_empty_group(app):
    app.ses_h.login(loginname="admin", password="secret")
    app.gr.create_group(Group(namegroup="", header="", footer=""))
    app.ses_h.logout()
