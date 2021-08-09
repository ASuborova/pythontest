import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture_create = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture_create
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture_create is None or not fixture_create.is_valid():
        fixture_create = Application(browser=browser, BUrl=web_config['BUrl'])
    fixture_create.ses_h.is_login(loginname=web_config['username'], password=web_config['password'])
    return fixture_create


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.district()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session")
def DBORM(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    db_orm_fixture = ORMFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])
    return db_orm_fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture_create.ses_h.is_logout()
        fixture_create.district()
    # yield fixture_create
    request.addfinalizer(fin)
    return fixture_create


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as file_json:
        return jsonpickle.decode(file_json.read())
