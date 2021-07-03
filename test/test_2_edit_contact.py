from model.contact import Contact


def test_edit_firstname_contact(app):
    app.cont_h.edit_first_contact(Contact(firstname="New_name", middlename=None, lastname="New_name", nickname=None, title=None,
                companyname=None, address=None,
                homephone=None, mobilephone=None,
                mainemail=None, email2="", bday=None, bmonth=None, byear=None))

