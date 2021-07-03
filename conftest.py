import pytest
from fixture.application import Application

fixture_create = None


@pytest.fixture
def app():
    global fixture_create
    if fixture_create is None:
        fixture_create = Application()
    else:
        if not fixture_create.is_valid():
            fixture_create = Application()
    fixture_create.ses_h.is_login(loginname="admin", password="secret")
    return fixture_create


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture_create.ses_h.is_logout()
        Application.district(fixture_create)
    # yield fixture_create
    request.addfinalizer(fin)
    return fixture_create
