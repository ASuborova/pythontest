from model.contact import Contact


def test_edit_contact(app):
    app.ses_h.login(loginname="admin", password="secret")
    app.cont_h.edit_first_contact(Contact(firstname="...", middlename="...", lastname="...", nickname="...", title="...",
                companyname="...", address="...",
                homephone="...", mobilephone="...",
                mainemail="...", email2="", bday="-",
                bmonth="-", byear="...."))
    app.ses_h.logout()
