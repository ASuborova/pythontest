def test_del_first_group(app):
    app.ses_h.login(loginname="admin", password="secret")
    app.gr.del_first_group()
    app.ses_h.logout()
