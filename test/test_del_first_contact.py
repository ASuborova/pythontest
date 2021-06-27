
def test_del_first_contact(app):
    app.ses_h.login(loginname="admin", password="secret")
    app.cont_h.del_first_contact()
    app.ses_h.logout()
