import pytest
from fixture.application import Application

fixture_create = None


@pytest.fixture
def app(request):
    global fixture_create
    browser = request.config.getoption("--browser")
    BUrl = request.config.getoption("--BUrl")
    if fixture_create is None:
        fixture_create = Application(browser=browser, BUrl=BUrl)
    else:
        if not fixture_create.is_valid():
            fixture_create = Application(browser=browser, BUrl=BUrl)
    fixture_create.ses_h.is_login(loginname="admin", password="secret")
    return fixture_create


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture_create.ses_h.is_logout()
        fixture_create.district()
    # yield fixture_create
    request.addfinalizer(fin)
    return fixture_create


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--BUrl", action="store", default="http://localhost/addressbook/index.php")
