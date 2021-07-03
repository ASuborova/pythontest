import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture_create = Application()
    fixture_create.ses_h.login(loginname="admin", password="secret")

    def fin():
        fixture_create.ses_h.logout()
        Application.district(fixture_create)
    # yield fixture_create
    request.addfinalizer(fin)
    return fixture_create
