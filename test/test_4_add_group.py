from model.group import Group


def test_add_group(app):
    app.gr.create_group(Group(namegroup="group_1", header="Zagolovok", footer="Podval"))


def test_add_empty_group(app):
    app.gr.create_group(Group())


