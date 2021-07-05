from model.group import Group


def test_del_first_group(app):
    if app.gr.count() == 0:
        app.gr.create_group(Group(namegroup="test", header=None, footer=None))
    app.gr.del_first_group()

